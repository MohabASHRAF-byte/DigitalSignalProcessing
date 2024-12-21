"""
This class serves as the base class for signal processing. It provides a flexible
framework for manipulating signals represented as a dictionary of index-value pairs.
Various signal operations (e.g., addition, subtraction, multiplication, etc.) and
transformations (e.g., mirroring, quantization, filtering) can be performed using
methods in this class.

Features:
- Arithmetic operations: addition, subtraction, multiplication, division
- Signal transformations: shifting, mirroring, averaging, differentiation
- Signal processing in the frequency domain: DFT, IDFT, filtering
- Quantization and error analysis
- Visualization: plotting signals

Note:
- All necessary imports are done internally within the methods
 to avoid circular dependencies.
"""


class Signal:

    def __init__(self, data: dict[int, float], offset: float = 0):
        """
        Initialize the signal with a dictionary of index-value
         pairs and an optional offset.

        :param data: A dictionary of index-value pairs representing the signal.
        :param offset: An optional offset for the signal (default is 0).
        """
        self.originalData = data.items()
        self.data = dict(sorted(data.items()))
        self.offset = offset
        if data and len(data):
            self.min_key = min(self.data.keys())
            self.max_key = max(self.data.keys())
        else:
            self.min_key = None
            self.max_key = None
        self.quantized_values = []
        self.errors = []
        self.levels = []
        self.encoded_values = []
        self.dft_amplitudes = []
        self.dft_phases = []
        self.len = len(data)

    def __str__(self):
        """
        Return a string representation of the signal, including its length and data.

        :return: A string representing the signal.
        """
        output = [f"Length of data: {len(self.data)}"]
        for k, v in self.data.items():
            output.append(f"{k}: {v}")
        return "\n".join(output)  # Combine lines into a single string

    def get_signal_indexs(self):
        """
        Get the indices (keys) of the signal.

        :return: A list of the signal's indices.
        """
        return list(self.data.keys())

    def get_signal_values(self):
        """
        Get the values of the signal.

        :return: A list of the signal's values.
        """
        return list(self.data.values())

    def __add__(self, other):
        """
        Add two signals or a signal and a scalar.

        This method uses the ArithmeticOperations class
        to apply the addition operation.

        :param other: The signal or scalar to add.
        :return: A new Signal object with the result of the addition.
        """
        from Functions.ArithmeticOperations import ArithmeticOperations
        return (ArithmeticOperations
                .apply_arithmetic_operation(self, other, lambda x, y: x + y))

    def __sub__(self, other):
        """
        Subtract two signals or a signal and a scalar.

        This method uses the ArithmeticOperations class
        to apply the subtraction operation.

        :param other: The signal or scalar to subtract.
        :return: A new Signal object with the result of the subtraction.
        """
        from Functions.ArithmeticOperations import ArithmeticOperations
        return (ArithmeticOperations
                .apply_arithmetic_operation(self, other, lambda x, y: x - y))

    def __mul__(self, other):
        """
        Multiply two signals or a signal and a scalar.

        This method uses the ArithmeticOperations class
        to apply the multiplication operation.

        :param other: The signal or scalar to multiply.
        :return: A new Signal object with the result of the multiplication.
        """
        from Functions.ArithmeticOperations import ArithmeticOperations
        return (ArithmeticOperations
                .apply_arithmetic_operation(self, other, lambda x, y: x * y))

    def __truediv__(self, other):
        """
        Divide two signals or a signal and a scalar.

        This method uses the ArithmeticOperations class
        to apply the division operation.
        If division by zero occurs, returns infinity.

        :param other: The signal or scalar to divide.
        :return: A new Signal object with the result of the division.
        """
        from Functions.ArithmeticOperations import ArithmeticOperations

        def divide_operation(x, y):
            return x / y if y != 0 else float('inf')

        return (ArithmeticOperations
                .apply_arithmetic_operation(self, other, divide_operation))

    def __repr__(self):
        """
        Return a string representation of the Signal object.

        :return: A string representation of the Signal object.
        """
        return f"Signal(data={self.data}, offset={self.offset})"

    def DelayingOrAdvancingSignalByK(self, k: int):
        """
        Apply a delaying or advancing operation to the signal by a factor of k.

        :param k: The factor by which to delay or advance the signal.
        """
        from Functions.delaying_or_advancing_signal import DelayingOrAdvancingSignal
        DelayingOrAdvancingSignal.apply(self, k)

    def mirror(self):
        """
        Apply a mirror transformation to the signal.
        """
        from Functions.mirror import Mirror
        Mirror.apply(self)

    def quantize_signal(self, perception=2, level=None, bits=None):
        """
        Quantize the signal with the given parameters.

        :param perception: The perception threshold (default is 2).
        :param level: The quantization levels (optional).
        :param bits: The number of bits for quantization (optional).
        """
        from Functions.quantize import Quantizer
        Quantizer.quantize(self, perception, level, bits)

    def Average(self, window_size: int, perception=2):
        """
        Apply an averaging operation to the signal using a window size and perception

        :param window_size: The size of the window for averaging.
        :param perception: The perception threshold (default is 2).
        """
        from Functions.average import Average
        Average.apply(self, window_size, perception)

    def derivative(self, n):
        """
        Compute the nth derivative of the signal.

        :param n: The order of the derivative.
        """
        from Functions.derivative import Derivative
        Derivative.apply(self, n)

    def convolve(self, s2: "Signal") -> "Signal":
        """
        Convolve this signal with another signal.

        :param s2: The second signal to convolve with.
        :return: A new Signal object with the result of the convolution.
        """
        from Functions.convolve import Convolve
        return Convolve.apply(self, s2)

    def apply_filter_in_frequency_domain(self, s2: "Signal") -> "Signal":
        """
        Apply a frequency domain filter to the signal.

        :param s2: The signal to apply the filter with.
        :return: A new Signal object with the filtered result.
        """
        from Functions.ApplyFrequencyFilter import Filter
        return Filter.apply(self, s2)

    def dft(self, fs: int):
        """
        Compute the Discrete Fourier Transform (DFT) of the signal.

        :param fs: The sampling frequency.
        :return: The DFT of the signal.
        """
        from Functions.dft_idft import DFT
        return DFT.compute_dft(self, fs)

    def idft(self, fs: int):
        """
        Compute the Inverse Discrete Fourier Transform (IDFT) of the signal.

        :param fs: The sampling frequency.
        :return: The IDFT of the signal.
        """
        from Functions.dft_idft import DFT
        return DFT.compute_idft(self, fs)

    def plot_signal(self, title="Signal Plot"):
        """
        Plot the signal using matplotlib in a tkinter window.

        :param title: The title of the plot (default is "Signal Plot").
        """
        from Functions.plot import Plot
        Plot.plot(self, title)

    def auto_correlate(self):
        """
        Compute the autoCorrelation of the signal.

        :return: A new Signal object with the autoCorrelation of the signal.
        """
        from Functions.auto_correlate import AutoCorrelation
        return AutoCorrelation.auto_correlate(self)
