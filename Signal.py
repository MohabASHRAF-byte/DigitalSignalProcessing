class Signal:
    def __init__(self, data: dict[int, float], offset: float = 0):
        """
        Initialize the signal with a dictionary
         of index-value pairs and an offset.
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
        # Construct a string representation
        output = [f"Length of data: {len(self.data)}"]
        for k, v in self.data.items():
            output.append(f"{k}: {v}")
        return "\n".join(output)  # Combine lines into a single string

    def get_signal_indexs(self):
        return list(self.data.keys())

    def get_signal_values(self):
        return list(self.data.values())

    def __add__(self, other):
        from Functions.ArithmeticOperations import ArithmeticOperations
        return (ArithmeticOperations
                .apply_arithmetic_operation(self, other, lambda x, y: x + y))

    def __sub__(self, other):
        from Functions.ArithmeticOperations import ArithmeticOperations
        return (ArithmeticOperations
                .apply_arithmetic_operation(self, other, lambda x, y: x - y))

    def __mul__(self, other):
        from Functions.ArithmeticOperations import ArithmeticOperations
        return (ArithmeticOperations
                .apply_arithmetic_operation(self, other, lambda x, y: x * y))

    def __truediv__(self, other):
        from Functions.ArithmeticOperations import ArithmeticOperations

        def divide_operation(x, y):
            return x / y if y != 0 else float('inf')

        return (ArithmeticOperations
                .apply_arithmetic_operation(self, other, divide_operation))

    def __repr__(self):
        return f"Signal(data={self.data}, offset={self.offset})"

    def DelayingOrAdvancingSignalByK(self, k: int):
        from Functions.delaying_or_advancing_signal import DelayingOrAdvancingSignal
        DelayingOrAdvancingSignal.apply(self, k)

    def mirror(self):
        from Functions.mirror import Mirror
        Mirror.apply(self)

    def quantize_signal(self, perception=2, level=None, bits=None):
        from Functions.quantize import Quantizer
        Quantizer.quantize(self, perception, level, bits)

    def Average(self, window_size: int, perception=2):
        from Functions.average import Average
        Average.apply(self, window_size, perception)

    def derivative(self, n):
        from Functions.derivative import Derivative
        Derivative.apply(self, n)

    def convolve(self, s2: "Signal") -> "Signal":
        from Functions.convolve import Convolve
        return Convolve.apply(self, s2)

    def apply_filter_in_frequency_domain(self, s2: "Signal") -> "Signal":
        from Functions.ApplyFrequencyFilter import Filter
        return Filter.apply(self, s2)

    def dft(self, fs: int):
        from Functions.dft_idft import DFT
        return DFT.compute_dft(self, fs)

    def idft(self, fs: int):
        from Functions.dft_idft import DFT
        return DFT.compute_idft(self, fs)

    def plot_signal(self, title="Signal Plot"):
        from Functions.plot import Plot
        Plot.plot(self, title)

    def auto_correlate(self):
        from Functions.auto_correlate import AutoCorrelation
        return AutoCorrelation.auto_correlate(self)
