import numpy as np
from scipy.optimize import least_squares


def almp(y, tol=1e-4, max_iter=200, fs=15360):

    n = len(y)  # Number of samples (signal time window)
    ts = 1/fs   # Sampling period
    t = np.arange(0, n) * ts

    # Algorithm results initialization
    a_n = list()
    f_n = list()
    theta_n = list()
    res_n = list()
    opt_res_n = list()

    # Algorithm execution
    res = y
    it = 1
    ss_t = np.zeros(y.shape)
    while it < max_iter:
        # Convert residue to frequency-domain
        ss_w = np.fft.fft(res)/n

        # Initial parameters selection
        idx_w_max = np.argmax(2*np.abs(ss_w[0: n//2]))
        w_0 = 2 * np.pi * idx_w_max * fs/n
        a_0 = 2 * np.abs(ss_w[idx_w_max])
        theta_0 = np.angle(ss_w[idx_w_max])
        x0 = np.array([a_0, w_0, theta_0])

        # Solve non-linear least square problem
        def fun(x):
            return res - x[0] * np.cos(x[1] * t + x[2])

        opt_res = least_squares(fun, x0, method='lm')
        a_n.append(opt_res.x[0])
        f_n.append(opt_res.x[1] / (2 * np.pi))
        theta_n.append(np.rad2deg(np.fmod(opt_res.x[2], 2 * np.pi)))
        opt_res_n.append(opt_res)

        # Make current atom
        atom = opt_res.x[0] * np.cos(opt_res.x[1] * t + np.fmod(opt_res.x[2], 2 * np.pi))

        # Residue update
        res = res - atom
        res_n.append(np.sqrt(np.sum(res ** 2)))

        # Stopping condition test
        if it > 1:
            diff = res_n[it - 2] - res_n[it - 1]
        else:
            diff = np.infty

        if diff < tol:
            if np.mean(atom ** 2) < tol:
                # Remove last
                a_n.pop()
                f_n.pop()
                theta_n.pop()
                res_n.pop()
                opt_res_n.pop()

            break
        else:
            ss_t = ss_t + atom
            it = it + 1

    return a_n, f_n, theta_n, ss_t, res, res_n, opt_res_n
