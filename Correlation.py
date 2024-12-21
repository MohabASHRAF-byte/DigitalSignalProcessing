import numpy as np
from Signal import Signal


def cross_correlation(s1: Signal, s2: Signal):
    n = s1.len
    s1_values = np.array(s1.get_signal_values())
    s2_values = np.array(s2.get_signal_values())

    norm_term = (
        np.sqrt(np.sum(s1_values ** 2)) * np.sqrt(np.sum(s2_values ** 2))
    )
    res = {}

    for shift in range(n):
        acc = 0
        for i in range(n):
            acc += s1_values[i] * s2_values[(i + shift) % n]

        res[shift] = acc / norm_term

    return res
