import numpy as np
from signal_generator import signal_names, signal_generator, wgn
from almp import almp
from ttictoc import tic, toc

if __name__ == '__main__':
    n_cycles = 12
    n_samples = 256
    fs = 15360

    n = n_samples * n_cycles
    ts = 1 / fs
    t = np.arange(0, n) * ts

    f = 60.0
    max_iter = 50

    # Signal choice
    phase = np.deg2rad(0.0)
    signal = signal_generator(t, signal_names['I'], f, phase)

    # Noise addition
    snr = 40.0
    noise = wgn(signal, snr)
    sigma = np.sqrt(np.mean(noise ** 2))
    if snr == 100.0:
        y = signal
    else:
        y = signal + noise

    tol = 4.0 * (np.mean(y ** 2) - np.mean(np.cos(2 * np.pi * f * t) ** 2))

    # Execute ALMP
    tic()
    a_n, f_n, theta_n, ss_t, res, res_n, opt_res_n = almp(y, tol, max_iter, fs)
    t_exp = toc()
    print(f'Execution time: {t_exp} s')

