from utilities import ReadSignal, CompSignals


class Task1Test:
    def AddationTest(self):
        signal1 = ReadSignal("Tests/Task1/Signal1.txt")
        signal2 = ReadSignal("Tests/Task1/Signal2.txt")
        signal3 = signal1 + signal2
        addSignal = ReadSignal("Tests/Task1/add.txt")
        print(CompSignals(signal3, addSignal, "Addation"))

    def SubtractiaonTest(self):
        signal1 = ReadSignal("Tests/Task1/Signal1.txt")
        signal2 = ReadSignal("Tests/Task1/Signal2.txt")
        signal3 = signal1 - signal2
        SubSignal = ReadSignal("Tests/Task1/subtract.txt")
        result = CompSignals(signal3, SubSignal, "Subtraction")
        print(result)

    def MulTest(self):
        signal1 = ReadSignal("Tests/Task1/Signal1.txt")
        signal3 = signal1 * 5
        mulBy5Signal = ReadSignal("Tests/Task1/mul5.txt")
        result = CompSignals(signal3, mulBy5Signal, "Mul5")
        print(result)

    def AdavnceTest(self):
        signal1 = ReadSignal("Tests/Task1/Signal1.txt")
        advance5 = ReadSignal("Tests/Task1/advance3.txt")
        signal1.DelayingOrAdvancingSignalByK(-3)
        result = CompSignals(signal1, advance5, "Advacning By 5 ")
        print(result)

    def DelayTest(self):
        signal1 = ReadSignal("Tests/Task1/Signal1.txt")
        delay5 = ReadSignal("Tests/Task1/delay3.txt")
        signal1.DelayingOrAdvancingSignalByK(3)
        result = CompSignals(signal1, delay5, "Delay By 5 ")
        print(result)

    def FoldingTest(self):
        signal1 = ReadSignal("Tests/Task1/Signal1.txt")
        mirror = ReadSignal("Tests/Task1/folding.txt")
        signal1.mirror()
        result = CompSignals(signal1, mirror, "Folding")
        print(result)

    def Task1TestRunner(self):
        print("Run Task 1 Tests ")
        print(".......................")
        self.AddationTest()
        self.SubtractiaonTest()
        self.MulTest()
        self.AdavnceTest()
        self.DelayTest()
        self.FoldingTest()
        print("*" * 50)
