from Correlation import cross_correlation
from Signal import Signal


def CalculateTimeDelay(s1: Signal, s2: Signal, fs: int):
    res = cross_correlation(s1, s2).values()
    maxi, idx = -1, -1
    for i, val in enumerate(res):
        if abs(val) > maxi:
            maxi = abs(val)
            idx = i
    return idx / fs
