from EquationParser import EquationParser
from Signal import Signal

dic = {
    - 4: - 2,
    - 3: 2,
    - 2: 0,
    - 1: 2,
    0: 4,
    1: 6,
    2: 3,
    3: 1,
    4: - 1,
    5: - 3,
    6: 0,
    7: 2
}
dic1 = {
    -3: 1,
    - 2: 0,
    - 1: - 1,
    0: 3,
    1: 2,
    2: 1,
    3: - 3,
    4: 6,
    5: 8,
    6: 3
}
variables = {
    "s1": Signal(data=dic, offset=5),
    "s2": Signal(data=dic1, offset=3)
}
s1 = Signal(data=dic)
ep = EquationParser(variables)
#Tests
add = ep.evaluate("s1 +s2")
sub = ep.evaluate("s1 - s2")
advance3 = s1.DelayingOrAdvancingSignalByK(-3)
Delay3 = s1.DelayingOrAdvancingSignalByK(3)
folding = s1.mirror()
mul5 = ep.evaluate("s1 * 5")

