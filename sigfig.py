import numpy as np
from math import log10, floor

def round_sig(x, sig=2):
    if x == 0:
        return 0
    elif x < 0:
        return -round(-x, sig-int(floor(log10(-x)))-1)
    return round(x, sig-int(floor(log10(x)))-1)
