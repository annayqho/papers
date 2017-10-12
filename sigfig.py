import numpy as np
from math import log10, floor

def round_sig(x, sig=2):
    if x == 0:
        return 0
    elif x < 0:
        return -round(-x, sig-int(floor(log10(-x)))-1)
    return round(x, sig-int(floor(log10(x)))-1)


def ndec(num):
    dec = str(num).split('.')[-1]
    return len(dec)


def format_val(val, sig):
    valrd = round_sig(val, 2) 
    sigrd = np.round(sig, ndec(valrd))
    val_str = str(valrd) + "$\pm$" + str(sigrd)
    if val < 0:
        val_str = ""
    return val_str
