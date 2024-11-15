import pandas as pd
from math import log2
class Signal:
    def __init__(self, data: dict[int, float], offset: float = 0):
            """Initialize the signal with a dictionary of index-value pairs and an offset."""
            self.data = dict(sorted(data.items()))
            self.offset = offset
            self.min_key = min(self.data.keys())
            self.max_key = max(self.data.keys())
            self.quantized_values = []  # Stores quantized values
            self.errors = []  # Stores errors for each quantized value
            self.levels = []  # Stores quantization levels
            self.encoded_values = []    # Stores encoded binary values for each quantized value

    def get_signal_indexs(self):
        return list(self.data.keys())

    def get_signal_values(self):
        return list(self.data.values())
    def do_work(self, other, op):
        """Helper function to apply an operation to two Signal objects or a Signal and a scalar."""
        if isinstance(other, Signal):
            idxs = sorted(set(self.data.keys()).union(other.data.keys()))
            result = {}
            for i in idxs:
                num1 = self.data.get(i, 0)
                num2 = other.data.get(i, 0)
                result[i] = op(num1, num2)
            return Signal(result, offset=self.offset)
        elif isinstance(other, (int, float)):
            # For scalar operation, apply it to all values in the Signal
            result = {i: op(self.data.get(i, 0), other) for i in self.data.keys()}
            return Signal(result, offset=self.offset)
        else:
            return NotImplemented

    def __add__(self, other):
        return self.do_work(other, lambda x, y: x + y)

    def __sub__(self, other):
        return self.do_work(other, lambda x, y: x - y)

    def __mul__(self, other):
        return self.do_work(other, lambda x, y: x * y)

    def __truediv__(self, other):
        return self.do_work(other, lambda x, y: x / y if y != 0 else float('inf'))

    def DelayingOrAdvancingSignalByK(self, k: int):
        result = {}
        for kk, v in self.data.items():
            result[kk + k] = v
        self.data = result
        
    

    def mirror(self):
        result = {}
        for k, v in self.data.items():
            result[k * -1] = v
        self.data = dict(sorted(result.items()))
        

    def __repr__(self):
        return f"Signal(data={self.data}, offset={self.offset})"

    def quantize_signal(self,perception=2, level=None, bits=None):
            """Perform signal quantization and store results in the class."""
            if not self.data:
                print("No signal data available.")
                return
            
            # Convert data values to a list for easier processing
            data_values = list(self.data.values())

            # Calculate minimum and maximum values from data
            min_val = min(data_values)
            max_val = max(data_values)

            # Determine levels based on the input (either number of levels or bits)
            if level is not None:
                levels = level
            elif bits is not None:
                levels = (1 << bits)
            else:
                print("Provide either levels or bits for quantization.")
                return

            # Calculate the delta and the actual quantization levels
            delta = (max_val - min_val) / levels
            self.levels = [round(min_val + i * delta + delta / 2,perception) for i in range(levels)]
            
            # Calculate binary representations of levels
            level_bits = int(log2(levels))
            binary_reprs = [bin(i)[2:].zfill(level_bits) for i in range(levels)]

            # Initialize lists to store quantization outputs and errors
            interval_indices = []
            encoded_values = []
            quantized_values = []
            errors = []
            output = []
            # Perform quantization
            for point in data_values:
                err = int(1e15)
                x = 0
                for i in range(levels):
                    if round(abs(point - self.levels[i]), perception) < err:
                        x = i
                        err = round(abs(point - self.levels[i]), perception)
                output.append([x + 1, binary_reprs[x], round(self.levels[x], perception), round(self.levels[x] - point, perception)])
                interval_indices.append(x + 1)
                encoded_values.append(binary_reprs[x])
                quantized_values.append(round(self.levels[x], perception))
                errors.append(round(self.levels[x] - point, perception))
            self.interval_indices= interval_indices
            self.quantized_values = quantized_values
            self.errors = errors
            self.levels = self.levels
            self.encoded_values = encoded_values
            # Output the quantization details
            # output = list(zip(interval_indices, encoded_values, quantized_values, errors))

