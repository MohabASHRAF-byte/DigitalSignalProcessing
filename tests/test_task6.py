from utilities import (
    ReadSignal,
    ReadSignalValues,
    CompSignalsBool
)
from Functions.Correlation import cross_correlation
from Signal import Signal
from Functions.TimeDelay import CalculateTimeDelay
from Functions.TemplateMatchingClss import TemplateMatching
from unittest import TestCase
from os.path import join
from pathlib import Path


class Task6Test(TestCase):
    base_path = Path(__file__).resolve().parent.parent / "Tests" / "Task6"

    def test_Correlation(self):
        inputPath1 = join(
            self.base_path,
            "CorrelationTest/input/Corr_input signal1.txt"
        )
        inputPath2 = join(
            self.base_path,
            "CorrelationTest/input/Corr_input signal2.txt"
        )
        outputPath = join(
            self.base_path,
            "CorrelationTest/output/CorrOutput.txt"
        )
        s1 = ReadSignal(inputPath1)
        s2 = ReadSignal(inputPath2)
        output = ReadSignal(outputPath)
        correlation_result = cross_correlation(s1, s2)
        s3 = Signal(correlation_result)
        self.assertTrue(
            CompSignalsBool(s3, output),
            "Test Correlation failed"
        )
        print("Correlation test passed successfully")

    def test_TimeDelay(self):
        inputPath1 = join(
            self.base_path,
            "TimeAnalysisTest/TD_input signal1.txt"
        )
        inputPath2 = join(
            self.base_path,
            "TimeAnalysisTest/TD_input signal2.txt"
        )
        s1 = ReadSignal(inputPath1)
        s2 = ReadSignal(inputPath2)
        fs = 100
        res = CalculateTimeDelay(s1, s2, fs)
        self.assertEqual(
            res, 5 / fs,
            "Test TimeDelay failed"
        )
        print("Time Delay test passed successfully")

    def test_TemplateMatching(self):
        inputPath1 = join(
            self.base_path,
            "TemplateMatching/Test Signals/Test1.txt"
        )
        inputPath2 = join(
            self.base_path,
            "TemplateMatching/Test Signals/Test2.txt"
        )
        s1 = ReadSignalValues(inputPath1)
        s2 = ReadSignalValues(inputPath2)
        tm = TemplateMatching()
        res1 = tm.classify(s1)
        res2 = tm.classify(s2)
        print(f"signal1 --> {res1}")
        print(f"signal2 --> {res2}")

    def Run(self):
        print("Task 6 Tests")
        print(50 * '-')
        self.test_Correlation()
        self.test_TimeDelay()
        self.test_TemplateMatching()
