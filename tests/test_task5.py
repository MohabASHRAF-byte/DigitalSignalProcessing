from utilities import (
    ReadSignal,
    ReadSignalInFrequencyDomain,
    SignalCompareAmplitude,
    SignalComparePhaseShift,
    CompSignalsBool
)
from unittest import TestCase
from os.path import join
from pathlib import Path


class Task5Test(TestCase):
    base_path = Path(__file__).resolve().parent.parent / "Tests" / "Task5"

    def test_DFT(self):
        inputPath = join(self.base_path, "DFT/input_Signal_DFT.txt")
        outputPath = join(self.base_path, "DFT/Output_Signal_DFT.txt")
        in_signal = ReadSignal(inputPath)
        out_signal = ReadSignalInFrequencyDomain(outputPath)
        in_signal.dft(8)
        self.assertTrue(
            SignalCompareAmplitude(in_signal, out_signal) and
            SignalComparePhaseShift(in_signal, out_signal),
            "Test DFT failed"
        )
        print("DFT test passed successfully")

    def test_IDFT(self):
        inputPath = join(self.base_path, "IDFT/Input_Signal_IDFT.txt")
        outputPath = join(self.base_path, "IDFT/Output_Signal_IDFT.txt")
        in_signal = ReadSignalInFrequencyDomain(inputPath)
        out_signal = ReadSignal(outputPath)
        in_signal.idft(8)
        self.assertTrue(
            CompSignalsBool(in_signal, out_signal),
            "Test IDFT failed"
        )
        print("IDFT test passed successfully")

    def Run(self):
        print("Task 5 Tests")
        print(50 * '-')
        self.test_DFT()
        self.test_IDFT()
