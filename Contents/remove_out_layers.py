import numpy as np

from .params import limit_inf, limit_sup

def remove_out_layers(A):

    A_copy = A.copy()

    mask = A <= limit_inf
    A_copy[mask] = limit_inf
    mask = A >= limit_sup
    A_copy[mask] = limit_sup

    return A_copy