"""
This class provides functionality to calculate the nth derivative of a signal.
The derivative is computed using a combination formula based on the order of
the derivative (n) and the signal values.
 Equation:
    #  x(n+1) - x(n)
    #  x(n+2) - 2x(n+1) + x(n)
    #  x(n) - 2x(n+1) + x(n+2)
# Ref/Combination Formula.png
"""

import math


class Derivative:
    @staticmethod
    def apply(signal, n):
        """Calculates the nth derivative of the signal."""
        limit = len(signal.data) - n
        keys, _ = zip(*signal.data.items())
        new_data = {}
        for i in range(limit):
            val = 0
            for k in range(n + 1):
                term1 = (-1) ** (k + (n % 2))
                term2 = math.comb(n, k)
                term3 = signal.data[keys[i + k]]
                val += term1 * term2 * term3
            new_data[keys[i]] = val

        signal.data = new_data
