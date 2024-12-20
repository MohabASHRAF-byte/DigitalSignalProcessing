import math

import pandas as pd
from math import log2
import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi, cos, sqrt, atan2
import math


class Signal:
    def __init__(self, data: dict[int, float], offset: float = 0):
        """Initialize the signal with a dictionary of index-value pairs and an offset."""
        self.originalData = data.items()
        self.data = dict(sorted(data.items()))
        self.offset = offset
        if data and len(data):
            self.min_key = min(self.data.keys())
            self.max_key = max(self.data.keys())
        else:
            self.min_key = None
            self.max_key = None
        self.quantized_values = []  # Stores quantized values
        self.errors = []  # Stores errors for each quantized value
        self.levels = []  # Stores quantization levels
        self.encoded_values = []  # Stores encoded binary values for each quantized value
        self.dft_amplitudes = []
        self.dft_phases = []
        self.len = len(data)
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

    def apply_filter_in_frequency_domain(self, s2: "Signal") -> "Signal":
        combined_length = len(self.data) + len(s2.data) - 1
        st = min(min(s2.data.keys()), min(self.data.keys()))
        ed = st + combined_length
        val1 = self.get_signal_values()
        val2 = s2.get_signal_values()
        x_padded = np.pad(val1, (0, combined_length - len(val1)))
        z_padded = np.pad(val2, (0, combined_length - len(val2)))
        data1 = {}
        data2 = {}
        for i, j in enumerate(range(st, ed)):
            data1[j] = x_padded[i]
            data2[j] = z_padded[i]

        self_padded_signal = Signal(data1)
        s2_padded_signal = Signal(data2)

        self_amp, self_phase= self_padded_signal.dft(combined_length)
        s2_amp, s2_phase= s2_padded_signal.dft(combined_length)

        convolved_amplitudes = [self_amp[i] * s2_amp[i] for i in range(combined_length)]
        convolved_phases = [(self_phase[i] + s2_phase[i]) for i in range(combined_length)]

        self.dft_amplitudes = convolved_amplitudes
        self.dft_phases = convolved_phases

        reconstructed_signal = self.idft(combined_length)
        data = {}
        for i, j in enumerate(range(st, ed)):
            data[j] = reconstructed_signal[i]
        return Signal(data)

    def dft(self, fs: int):
        """
        Perform Discrete Fourier Transform on the input signal.
        :param fs: sampling frequency
        :return: List of [Amplitude, Phase] for each frequency component
        """
        _, input_signal = zip(*self.data.items())

        N = len(input_signal)
        amplitudes, phases = [], []
        fs = min(N, fs)
        for k in range(fs):
            real, imag = 0, 0
            for j in range(N):
                termVal = 2 * pi * k * j / N
                real += input_signal[j] * cos(termVal)
                imag += -input_signal[j] * sin(termVal)

            amplitude = sqrt(real ** 2 + imag ** 2)  # Amplitude
            phase = atan2(imag, real)  # Phase
            amplitudes.append(amplitude)
            phases.append(phase)
        self.dft_amplitudes = amplitudes
        self.dft_phases = phases
        return amplitudes, phases

    def idft(self, fs):
        """
        Perform Inverse Discrete Fourier Transform to reconstruct the signal.
        :param fs: sampled frequency
        :return: List of reconstructed real values (time domain signal)
        """
        N = min(fs, len(self.dft_amplitudes))
        reconstructed_signal = []
        for k in range(N):
            real = 0
            for n in range(N):
                amplitude, phase = self.dft_amplitudes[n], self.dft_phases[n]
                term_val = 2 * pi * k * n / N  # IDFT formula
                real += amplitude * cos(term_val + phase)  # Reconstruct real part
            reconstructed_signal.append(real / N)  # Normalize the result
        self.data.clear()
        for i in range(len(reconstructed_signal)):
            self.data[i] = reconstructed_signal[i]
        return reconstructed_signal  # Return reconstructed real values
