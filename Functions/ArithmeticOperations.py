"""
Apply the passed operation to the signal
"""
from Signal import Signal


class ArithmeticOperations:
    @staticmethod
    def apply_arithmetic_operation(signal1, signal2, op):
        """
        Apply an arithmetic operation to two Signal objects or a Signal and a scalar.
        """
        if isinstance(signal2, Signal):
            idxs = sorted(set(signal1.data.keys()).union(signal2.data.keys()))
            result = {}
            for i in idxs:
                num1 = signal1.data.get(i, 0)
                num2 = signal2.data.get(i, 0)
                result[i] = op(num1, num2)
            return Signal(result, offset=signal1.offset)
        elif isinstance(signal2, (int, float)):
            # For scalar operation, apply it to all values in the Signal
            result = {
                i: op(signal1.data.get(i, 0), signal2) for i in signal1.data.keys()
            }
            return Signal(result, offset=signal1.offset)
        else:
            return NotImplemented
