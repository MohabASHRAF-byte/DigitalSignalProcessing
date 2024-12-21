from utilities import ReadSignal, CompSignals, CompSignalsBool
from unittest import TestCase
import os
from os.path import join
from pathlib import Path


class Task4Test(TestCase):
    base_path = Path(__file__).resolve().parent.parent / "Tests" / "Task4"

    def test_Move_Avg_1(self):
        inputPath = join(self.base_path, "Moving_Average/MovingAvg_input.txt")
        outputPath = join(self.base_path, "Moving_Average/MovingAvg_out1.txt")
        in_signal = ReadSignal(inputPath)
        out_signal = ReadSignal(outputPath)
        in_signal.Average(window_size=3, perception=3)
        self.assertTrue(
            CompSignalsBool(in_signal, out_signal),
            "Test Moving Average Window = 3 failed"
        )
        print("Moving Average Window = 3 test passed successfully")

    def test_Move_Avg_2(self):
        inputPath = join(self.base_path, "Moving_Average/MovingAvg_input.txt")
        outputPath = join(self.base_path, "Moving_Average/MovingAvg_out2.txt")
        in_signal = ReadSignal(inputPath)
        out_signal = ReadSignal(outputPath)
        in_signal.Average(window_size=5, perception=1)
        self.assertTrue(
            CompSignalsBool(in_signal, out_signal),
            "Test Moving Average Window = 5 failed"
        )
        print("Moving Average Window = 5 test passed successfully")

    def test_Derivative_1(self):
        inputPath = join(self.base_path, "Derivative/Derivative_input.txt")
        outputPath = join(self.base_path, "Derivative/1st_derivative_out.txt")
        in_signal = ReadSignal(inputPath)
        out_signal = ReadSignal(outputPath)
        in_signal.derivative(1)
        self.assertTrue(
            CompSignalsBool(in_signal, out_signal),
            "Test 1st Derivative failed"
        )
        print("1st Derivative test passed successfully")

    def test_Derivative_2(self):
        inputPath = join(self.base_path, "Derivative/Derivative_input.txt")
        outputPath = join(self.base_path, "Derivative/2nd_derivative_out.txt")
        in_signal = ReadSignal(inputPath)
        out_signal = ReadSignal(outputPath)
        in_signal.derivative(2)
        self.assertTrue(
            CompSignalsBool(in_signal, out_signal),
            "Test 2nd Derivative failed"
        )
        print("2nd Derivative test passed successfully")

    def test_Convolution(self):
        inputPath1 = join(self.base_path, "Convolution/Signal 1.txt")
        inputPath2 = join(self.base_path, "Convolution/Signal 2.txt")
        outputPath = join(self.base_path, "Convolution/Conv_output.txt")
        in_signal1 = ReadSignal(inputPath1)
        in_signal2 = ReadSignal(inputPath2)
        out_signal = ReadSignal(outputPath)
        out2 = in_signal1.convolve(in_signal2)
        self.assertTrue(
            CompSignalsBool(out2, out_signal),
            "Test Convolution failed"
        )
        print("Convolution test passed successfully")

    def Run(self):
        print("Task 4 Tests")
        print(50 * '-')
        self.test_Move_Avg_1()
        self.test_Move_Avg_2()
        self.test_Derivative_1()
        self.test_Derivative_2()
        self.test_Convolution()
