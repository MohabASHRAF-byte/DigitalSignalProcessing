# quantize.py

from math import log2


class Quantizer:
    @staticmethod
    def quantize(signal, perception=2, level=None, bits=None):
        if not signal.data:
            print("No signal data available.")
            return

        data_values = list(signal.data.values())
        min_val = min(data_values)
        max_val = max(data_values)

        if level is not None:
            levels = level
        elif bits is not None:
            levels = (1 << bits)
        else:
            print("Provide either levels or bits for quantization.")
            return

        delta = (max_val - min_val) / levels
        signal.levels = \
            [round(min_val + i * delta + delta / 2, perception)
             for i in range(levels)]
        level_bits = int(log2(levels))
        binary_reprs = [bin(i)[2:].zfill(level_bits) for i in range(levels)]

        interval_indices, encoded_values, quantized_values, errors = [], [], [], []
        for point in data_values:
            err = int(1e15)
            x = 0
            for i in range(levels):
                if round(abs(point - signal.levels[i]), perception) < err:
                    x = i
                    err = round(abs(point - signal.levels[i]), perception)
            interval_indices.append(x + 1)
            encoded_values.append(binary_reprs[x])
            quantized_values.append(round(signal.levels[x], perception))
            errors.append(round(signal.levels[x] - point, perception))

        signal.interval_indices = interval_indices
        signal.quantized_values = quantized_values
        signal.errors = errors
        signal.encoded_values = encoded_values
