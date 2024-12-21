"""
This class provides the functionality to compute the autocorrelation of a signal.
"""

from Signal import Signal


class AutoCorrelation:
    @staticmethod
    def auto_correlate(signal: Signal) -> Signal:
        """
        Computes the autocorrelation of the signal.
        """
        values = list(signal.data.values())
        N = len(values)
        autocorr = {}

        for lag in range(-N + 1, N):
            sum_val = \
                sum(values[i] * values[i + lag]
                    for i in range(N) if 0 <= i + lag < N)
            autocorr[lag] = sum_val

        return Signal(autocorr)
