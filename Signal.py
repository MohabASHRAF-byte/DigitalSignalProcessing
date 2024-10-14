class Signal:
    def __init__(self, data: dict[int, float], offset: float = 0):
        """Initialize the signal with a dictionary of index-value pairs and an offset."""
        self.data = dict(sorted(data.items()))
        self.offset = offset
        self.min_key = min(self.data.keys())
        self.max_key = max(self.data.keys())

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
        return Signal(result)

    def mirror(self):
        result = {}
        for k, v in self.data.items():
            result[k * -1] = v
        return Signal(result)

    def __repr__(self):
        return f"Signal(data={self.data}, offset={self.offset})"
