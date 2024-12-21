from unittest import TestCase
from os.path import join
from utilities import ReadSignal, CompSignals, CompSignalsBool
from pathlib import Path


class Task1Test(TestCase):
    base_path = Path(__file__).resolve().parent.parent / "Tests" / "Task1"

    def test_addation(self):
        signal1path = join(self.base_path, "Signal1.txt")
        signal2path = join(self.base_path, "Signal2.txt")
        outputPath = join(self.base_path, "add.txt")
        signal1 = ReadSignal(signal1path)
        signal2 = ReadSignal(signal2path)
        addSignal = ReadSignal(outputPath)
        signal3 = signal1 + signal2
        self.assertTrue(
            CompSignalsBool(signal3, addSignal),
            "Test add two signals failed"
        )
        print("Addation passed successfully")

    def test_Subtraction(self):
        signal1path = join(self.base_path, "Signal1.txt")
        signal2path = join(self.base_path, "Signal2.txt")
        outputPath = join(self.base_path, "subtract.txt")
        signal1 = ReadSignal(signal1path)
        signal2 = ReadSignal(signal2path)
        SubSignal = ReadSignal(outputPath)
        signal3 = signal1 - signal2
        self.assertTrue(
            CompSignalsBool(signal3, SubSignal),
            "Test Subtraction two signals failed"
        )
        print("Test Subtraction passed Successfully")

    def test_MulTest(self):
        signal1path = join(self.base_path, "Signal1.txt")
        outputPath = join(self.base_path, "mul5.txt")
        signal1 = ReadSignal(signal1path)
        mulSignal = ReadSignal(outputPath)
        signal3 = signal1 * 5
        self.assertTrue(
            CompSignalsBool(signal3, mulSignal),
            "Test multiplication by 5 failed"
        )
        print("Multiplication test passed successfully")

    def test_Advance(self):
        signal1path = join(self.base_path, "Signal1.txt")
        outputPath = join(self.base_path, "advance3.txt")
        signal1 = ReadSignal(signal1path)
        advanceSignal = ReadSignal(outputPath)
        signal1.DelayingOrAdvancingSignalByK(-3)
        self.assertTrue(
            CompSignalsBool(signal1, advanceSignal),
            "Test advancing by 3 failed"
        )
        print("Advance test passed successfully")

    def test_Delay(self):
        signal1path = join(self.base_path, "Signal1.txt")
        outputPath = join(self.base_path, "delay3.txt")
        signal1 = ReadSignal(signal1path)
        delaySignal = ReadSignal(outputPath)
        signal1.DelayingOrAdvancingSignalByK(3)
        self.assertTrue(
            CompSignalsBool(signal1, delaySignal),
            "Test delay by 3 failed"
        )
        print("Delay test passed successfully")

    def test_Folding(self):
        signal1path = join(self.base_path, "Signal1.txt")
        outputPath = join(self.base_path, "folding.txt")
        signal1 = ReadSignal(signal1path)
        foldSignal = ReadSignal(outputPath)
        signal1.mirror()
        self.assertTrue(
            CompSignalsBool(signal1, foldSignal),
            "Test folding failed"
        )
        print("Folding test passed successfully")

    def Run(self):
        print("Run Task 1 Tests ")
        print(".......................")
        self.test_addation()
        self.test_Subtraction()
        self.test_MulTest()
        self.test_Advance()
        self.test_Delay()
        self.test_Folding()
