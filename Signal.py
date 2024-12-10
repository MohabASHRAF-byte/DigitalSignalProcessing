import math

import pandas as pd
from math import log2
import numpy as np
import matplotlib.pyplot as plt


class Signal:
    def __init__(self, data: dict[int, float], offset: float = 0):
        """Initialize the signal with a dictionary of index-value pairs and an offset."""
        self.originalData = data.items()
        self.data = dict(sorted(data.items()))
        self.offset = offset
        self.min_key = min(self.data.keys())
        self.max_key = max(self.data.keys())
        self.quantized_values = []  # Stores quantized values
        self.errors = []  # Stores errors for each quantized value
        self.levels = []  # Stores quantization levels
        self.encoded_values = []  # Stores encoded binary values for each quantized value

    def __str__(self):
        # Construct a string representation
        output = [f"Length of data: {len(self.data)}"]
        for k, v in self.data.items():
            output.append(f"{k}: {v}")
        return "\n".join(output)  # Combine lines into a single string

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

    def quantize_signal(self, perception=2, level=None, bits=None):
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
        self.levels = [round(min_val + i * delta + delta / 2, perception) for i in range(levels)]

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
            output.append(
                [x + 1, binary_reprs[x], round(self.levels[x], perception), round(self.levels[x] - point, perception)])
            interval_indices.append(x + 1)
            encoded_values.append(binary_reprs[x])
            quantized_values.append(round(self.levels[x], perception))
            errors.append(round(self.levels[x] - point, perception))
        self.interval_indices = interval_indices
        self.quantized_values = quantized_values
        self.errors = errors
        self.levels = self.levels
        self.encoded_values = encoded_values
        # Output the quantization details
        # output = list(zip(interval_indices, encoded_values, quantized_values, errors))

    def Average(self, window_size: int, perception=2):
        limit = len(self.data) - window_size + 1
        keys, _ = zip(*self.data.items())
        new_data = {}
        for i in range(limit):
            s = 0
            for j in range(window_size):
                key = keys[i + j]
                s += self.data[key]
            new_data[keys[i]] = round(s / window_size, perception)
        self.data = new_data

    #  x(n+1) - x(n)
    #  x(n+2) - 2x(n+1) + x(n)
    #  x(n) - 2x(n+1) + x(n+2)
    #  Ref/Combination Formula.png

    def derivative(self, n):
        limit = len(self.data) - n
        keys, _ = zip(*self.data.items())
        new_data = {}
        for i in range(limit):
            val = 0
            for k in range(n + 1):
                term1 = (-1) ** (k + (n % 2))
                term2 = math.comb(n, k)
                term3 = self.data[keys[i + k]]
                val += term1 * term2 * term3
            new_data[keys[i]] = val

        self.data = new_data

    def convolve(self, s2: "Signal") -> "Signal":
        if not isinstance(s2, Signal):
            raise ValueError("Argument must be an instance of Signal")

        keys1, values1 = zip(*self.data.items())
        keys2, values2 = zip(*s2.data.items())

        result = {}

        for i, k1 in enumerate(keys1):
            for j, k2 in enumerate(keys2):
                k_res = k1 + k2  # New index
                result[k_res] = result.get(k_res, 0) + values1[i] * values2[j]

        return Signal(result)

    def dft(self, sampling_frequency):
        if not self.data:
            print("No signal data available.")
            return

        signal_values = np.array(self.get_signal_values())
        n = len(signal_values)
        dft_result = []

        for k in range(n):
            real = sum(signal_values[m] * np.cos(2 * np.pi * k * m / n) for m in range(n))
            imag = sum(-signal_values[m] * np.sin(2 * np.pi * k * m / n) for m in range(n))
            dft_result.append(complex(real, imag))

        dft_result = np.array(dft_result)

        freq = np.fft.fftfreq(n, d=1 / sampling_frequency)
        amplitude = np.abs(dft_result)

        # Plot Frequency vs Amplitude
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 1, 1)
        plt.plot(freq[:n // 2], amplitude[:n // 2])
        plt.title("Frequency vs Amplitude (DFT)")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.grid()

        # Plot Frequency vs Phase
        phase = np.angle(dft_result)
        plt.subplot(2, 1, 2)
        plt.plot(freq[:n // 2], phase[:n // 2])
        plt.title("Frequency vs Phase (DFT)")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Phase (radians)")
        plt.grid()

        plt.tight_layout()
        plt.show()

        print(freq, amplitude, dft_result)
        dft_data = {freq[i]: amplitude[i] for i in range(len(freq))}

        return Signal(dft_data, offset=self.offset)

    def idft(self, sampling_frequency):
        # Retrieve the signal values
        if not self.data:
            print("No signal data available.")
            return None

        signal_values = np.array(self.get_signal_values())
        n = len(signal_values)

        idft_result = []

        for m in range(n):
            real = sum(signal_values[k] * np.cos(2 * np.pi * k * m / n) for k in range(n))
            imag = sum(signal_values[k] * np.sin(2 * np.pi * k * m / n) for k in range(n))
            idft_result.append((real + imag) / n)

        idft_result = np.array(idft_result)

        # Get the original signal indices (time steps)
        keys = self.get_signal_indexs()

        # Create a new Signal object with reconstructed values
        reconstructed_data = {keys[i]: idft_result[i] for i in range(len(keys))}
        return Signal(reconstructed_data, offset=self.offset)