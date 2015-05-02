"""
Default configurations

"""

__author__ = 'noe'

import numpy as np
import logging

# compute kernel. Could be 'c' or 'python'
kernel = 'c'

# data type for floating-point operations. Use np.float32 or np.float64
dtype = np.float64

# print a lot of info?
verbose = True


def log_level():
    if verbose:
        return logging.INFO
    else:
        return logging.DEBUG
