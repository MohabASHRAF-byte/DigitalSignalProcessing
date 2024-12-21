"""
This class provides functionality to mirror a signal.
The signal is mirrored by flipping the indices of the data
    (multiplying each index by -1)
and reordering the signal values accordingly.
"""


class Mirror:
    @staticmethod
    def apply(signal):
        """Mirrors the signal."""
        result = {}
        for k, v in signal.data.items():
            result[k * -1] = v
        signal.data = dict(sorted(result.items()))
