"""
This class provides functionality to delay or advance a signal by a specified
number of units (k). The method shifts the indices of the signal data
without altering the values.
"""


class DelayingOrAdvancingSignal:
    @staticmethod
    def apply(signal, k: int):
        """Delays or advances the signal by k units."""
        result = {}
        for kk, v in signal.data.items():
            result[kk + k] = v
        signal.data = result
