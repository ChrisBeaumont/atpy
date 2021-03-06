from __future__ import print_function, division

import numpy as np


def smart_mask(array, null):
    if type(null) in [float, np.float32, np.float64]:
        if np.isnan(null):
            return np.isnan(array)
        else:
            return array == null
    else:
        return array == null


def smart_dtype(dtype):
    if dtype.subdtype:
        return dtype.subdtype[0].type
    else:
        return dtype.type


def format_length(format):
    if '.' in format:
        return int(format.split('.')[0])
    else:
        return int(format[:-1])
