# ALMP
The anti-leakage matching pursuit (ALMP) algorithm can estimate harmonics and interharmonics mainly under noise and frequency deviations. The algorithm is based on the Matching Pursuit method, and its principal stage consists of solving a non-linear least squares problem.

The file `almp.py` contains the algorithms' implementation. The file `signal_generator.py` has functions to generate synthetic signals for analysis and a function for adding Gaussian white noise to signals. The file `main.py` has an example of using the ALMP algorithm.