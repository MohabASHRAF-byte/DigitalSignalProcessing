from EquationParser import EquationParser
from Signal import Signal
def test():
    dic = {
    0 :0.387,
    1: 0.430,
    2 :0.478,
    3: 0.531,
    4: 0.590,
    5 :0.6561,
    6 :0.729,
    7 :0.81,
    8 :0.9,
    9 :1,
    10: 0.2,
    }
    dic1={
    0 :-1.22,
    1 :1.5,
    2: 3.24,
    3 :3.94,
    4 :2.20,
    5 :-1.1,
    6 :-2.26,
    7 :-1.88,
    8 :-1.2,
    }
    s1 = Signal(data=dic1)
    s1.quantize_signal(bits=2)
    print(s1.quantized_values)
    print(s1.errors)
