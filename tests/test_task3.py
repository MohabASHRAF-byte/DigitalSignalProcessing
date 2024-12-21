import utilities
from Signal import Signal
from unittest import TestCase
from pathlib import Path
from os.path import join

from utilities import ReadSignal, CompSignalsQuantized, CompSignalsQuantized2


class QuantizationTest(TestCase):
    inputFilePath = [f"Tests/Task3/Test1/in.txt", f"Tests/Task3/Test2/in.txt"]
    outputFilePath = [f"Tests/Task3/Test1/out.txt", f"Tests/Task3/Test2/out.txt"]
    base_path = Path(__file__).resolve().parent.parent / "Tests" / "Task3"

    def GetTestSignal(self, index: int):
        index -= 1
        if index >= len(self.inputFilePath):
            return -1
        filePath = self.inputFilePath[index]
        return utilities.ReadSignal(filePath)

    def GetTestOutputPath(self, index: int):
        index -= 1
        if index >= len(self.outputFilePath):
            return -1
        return self.outputFilePath[index]

    def test_Test1(self):
        signal = ReadSignal(join(self.base_path, "Test1/in.txt"))
        outputPath = join(self.base_path, "Test1/out.txt")
        signal.quantize_signal(perception=3, level=8)
        self.assertTrue(CompSignalsQuantized(signal, outputPath))

    def test_Test2(self):
        signal = ReadSignal(join(self.base_path, "Test2/in.txt"))
        outputPath = join(self.base_path, "Test2/out.txt")
        signal.quantize_signal(perception=2, bits=2)
        self.assertTrue(CompSignalsQuantized2(signal, outputPath))

    def Run(self):
        print("Run Task 3 Tests")
        print(".......................")
        signal1 = self.GetTestSignal(1)
        signal1.quantize_signal(level=8)
        signal2 = self.GetTestSignal(2)
        signal2.quantize_signal(level=4)
        Tester = QuantizationTest()
        Tester.test_Test1()
        # Tester.Test2(signal=signal2)
