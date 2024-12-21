"""
This class provides functionality to apply a moving average filter to a signal.
The filter is applied with a specified window size, and the signal values are
averaged over that window to smooth the data.
"""


class Average:
    @staticmethod
    def apply(signal, window_size: int, perception=2):
        """Applies an average filter of given window size."""
        limit = len(signal.data) - window_size + 1
        keys, _ = zip(*signal.data.items())
        new_data = {}
        for i in range(limit):
            s = 0
            for j in range(window_size):
                key = keys[i + j]
                s += signal.data[key]
            new_data[keys[i]] = round(s / window_size, perception)
        signal.data = new_data
