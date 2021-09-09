import numpy as np

from .params import limit_up, limit_down

def remove_out_layers(A):

    A_copy = A.copy()

    mask = A <= limit_down
    A_copy[mask] = limit_down
    mask = A >= limit_up
    A_copy[mask] = limit_up

    return A_copy