"""
This class provides functionality to convolve two signals together.
The convolution is performed by summing the product of the signals over
all possible overlapping positions of the indices.
"""
from Signal import Signal


class Convolve:
    @staticmethod
    def apply(signal, s2: "Signal") -> "Signal":
        """Convolve two signals."""
        if not isinstance(s2, Signal):
            raise ValueError("Argument must be an instance of Signal")

        keys1, values1 = zip(*signal.data.items())
        keys2, values2 = zip(*s2.data.items())

        result = {}

        for i, k1 in enumerate(keys1):
            for j, k2 in enumerate(keys2):
                k_res = k1 + k2  # New index
                result[k_res] = result.get(k_res, 0) + values1[i] * values2[j]

        return Signal(result)
