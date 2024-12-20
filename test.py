from Signal import Signal

s1 = Signal({
    0: 1,
    1: 2,
    2: 2,
    3: 1
})
fil = Signal({
    0: 1,
    1: 2,
    2: 3
})

Amp1, ph1 = s1.dft(500)
Amp2, ph2 = fil.dft(500)
print(Amp1)
print(ph1)
print('*' * 100)
print(Amp2)
print(ph2)
