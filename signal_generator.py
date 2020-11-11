import numpy as np


def wgn(signal, snr=40.0):
    eps = 10 ** (-snr / 10)
    return np.random.normal(0, np.sqrt(np.mean(signal ** 2) * eps), len(signal))


signal_names = {'I': 'Single-phase rectifier',
                'II': 'Six-pulse converter',
                'III': 'Synchronous machine',
                'IV': 'Microgrid',
                'V': 'Overexcited transformer',
                'VI': 'Single harmonic-interharmonic'}


def signal_generator(t, name, f, ph):
    y = np.zeros(t.shape)
    if name == 'Single-phase rectifier':
        i_dc = 1.0 / (2.0 * np.sqrt(2))
        y = (2.0 * np.sqrt(2) / 1.0) * i_dc * np.sin(2 * np.pi * f * 1 * t + np.deg2rad(ph)) \
            + (2.0 * np.sqrt(2) / 5.0) * i_dc * np.sin(2 * np.pi * f * 5 * t + np.deg2rad(ph)) \
            + (2.0 * np.sqrt(2) / 9.0) * i_dc * np.sin(2 * np.pi * f * 9 * t + np.deg2rad(ph)) \
            + (2.0 * np.sqrt(2) / 13.0) * i_dc * np.sin(2 * np.pi * f * 13 * t + np.deg2rad(ph)) \
            - (2.0 * np.sqrt(2) / 3.0) * i_dc * np.sin(2 * np.pi * f * 3 * t + np.deg2rad(ph)) \
            - (2.0 * np.sqrt(2) / 7.0) * i_dc * np.sin(2 * np.pi * f * 7 * t + np.deg2rad(ph)) \
            - (2.0 * np.sqrt(2) / 11.0) * i_dc * np.sin(2 * np.pi * f * 11 * t + np.deg2rad(ph)) \
            - (2.0 * np.sqrt(2) / 15.0) * i_dc * np.sin(2 * np.pi * f * 15 * t + np.deg2rad(ph))

    elif name == 'Six-pulse converter':
        i_1 = 1
        y = i_1 * np.cos(2 * np.pi * f * t) \
            - (1/5) * i_1 * np.cos(5 * 2 * np.pi * f * t + np.deg2rad(ph)) \
            + (1/7) * i_1 * np.cos(7 * 2 * np.pi * f * t + np.deg2rad(ph)) \
            - (1/11) * i_1 * np.cos(11 * 2 * np.pi * f * t + np.deg2rad(ph)) \
            + (1/13) * i_1 * np.cos(13 * 2 * np.pi * f * t + np.deg2rad(ph)) \
            - (1/17) * i_1 * np.cos(17 * 2 * np.pi * f * t + np.deg2rad(ph)) \
            + (1/19) * i_1 * np.cos(19 * 2 * np.pi * f * t + np.deg2rad(ph)) \
            - (1/23) * i_1 * np.cos(23 * 2 * np.pi * f * t + np.deg2rad(ph)) \
            + (1/25) * i_1 * np.cos(25 * 2 * np.pi * f * t + np.deg2rad(ph))

    elif name == 'Synchronous machine':
        y = 0.030 * np.sin(2 * np.pi * 0.4 * f * t + np.deg2rad(ph)) \
            + 0.024 * np.sin(2 * np.pi * 0.8 * f * t + np.deg2rad(ph)) \
            + 1.000 * np.sin(2 * np.pi * 1.0 * f * t + np.deg2rad(ph)) \
            + 0.023 * np.sin(2 * np.pi * 1.6 * f * t + np.deg2rad(ph)) \
            + 0.029 * np.sin(2 * np.pi * 4.4 * f * t + np.deg2rad(ph)) \
            + 0.030 * np.sin(2 * np.pi * 6.4 * f * t + np.deg2rad(ph)) \
            + 0.003 * np.sin(2 * np.pi * 9.8 * f * t + np.deg2rad(ph)) \
            + 0.004 * np.sin(2 * np.pi * 11.8 * f * t + np.deg2rad(ph))

    elif name == 'Overexcited transformer':
        y = 1 * np.cos(2 * np.pi * f * t + ph) \
            - 0.18 * np.cos(2 * np.pi * 3 * f * t + np.deg2rad(ph)) \
            + 0.11 * np.cos(2 * np.pi * 5 * f * t + np.deg2rad(ph))

    elif name == 'Single harmonic-interharmonic':
        y = np.cos(2 * np.pi * f * t + np.deg2rad(30)) \
            + 0.3 * np.cos(2 * np.pi * 3 * f * t + np.deg2rad(-10)) \
            + 0.1 * np.cos(2 * np.pi * 222 * t)

    elif name == 'Microgrid':
        y = 0.0026 * np.cos(2 * np.pi * 19.92 * t + np.deg2rad(-157.34)) \
            + 1 * np.cos(2 * np.pi * 49.8 * t + np.deg2rad(147.49)) \
            + 0.0015 * np.cos(2 * np.pi * 229.08 * t + np.deg2rad(78.94)) \
            + 0.0302 * np.cos(2 * np.pi * 249 * t + np.deg2rad(101.91)) \
            + 0.0245 * np.cos(2 * np.pi * 348.6 * t + np.deg2rad(-145.68))

    return y
