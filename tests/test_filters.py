from filters import get_filters
from utilities import ReadSignal, CompSignals
from unittest import TestCase
from pathlib import Path
from os.path import join


class PracticalFiltersTest(TestCase):
    base_path = Path(__file__).resolve().parent.parent / "Tests" / "Practical" / "FIR test cases"

    def test_lowPass_coefficients(self):
        filterLowPass = get_filters("Low pass", 8000, 50, 1500, None, 500)
        expected_signal = ReadSignal(join(self.base_path, "Testcase 1/LPFCoefficients.txt"))
        self.assertTrue(CompSignals(filterLowPass, expected_signal, "Test case 1"))

    def test_lowPass_timeDomain(self):
        filterLowPass = get_filters("Low pass", 8000, 50, 1500, None, 500)
        testSignal = ReadSignal(join(self.base_path, "Testcase 2/ecg400.txt"))
        expected_signal = ReadSignal(join(self.base_path, "Testcase 2/ecg_low_pass_filtered.txt"))

        filteredSignal = testSignal.convolve(filterLowPass)
        self.assertTrue(CompSignals(filteredSignal, expected_signal, "Test case 2 (Time Domain)"))

    def test_lowPass_frequencyDomain(self):
        filterLowPass = get_filters("Low pass", 8000, 50, 1500, None, 500)
        testSignal = ReadSignal(join(self.base_path, "Testcase 2/ecg400.txt"))
        expected_signal = ReadSignal(join(self.base_path, "Testcase 2/ecg_low_pass_filtered.txt"))

        filteredSignal = testSignal.apply_filter_in_frequency_domain(filterLowPass)
        self.assertTrue(CompSignals(filteredSignal, expected_signal, "Test case 2 (Frequency Domain)"))

    def test_highPass_coefficients(self):
        filterHighPass = get_filters("High pass", 8000, 70, 1500, None, 500)
        expected_signal = ReadSignal(join(self.base_path, "Testcase 3/HPFCoefficients.txt"))
        self.assertTrue(CompSignals(filterHighPass, expected_signal, "Test case 3"))

    def test_highPass_timeDomain(self):
        filterHighPass = get_filters("High pass", 8000, 70, 1500, None, 500)
        testSignal = ReadSignal(join(self.base_path, "Testcase 4/ecg400.txt"))
        expected_signal = ReadSignal(join(self.base_path, "Testcase 4/ecg_high_pass_filtered.txt"))

        filteredSignal = testSignal.convolve(filterHighPass)
        self.assertTrue(CompSignals(filteredSignal, expected_signal, "Test case 4 (Time Domain)"))

    def test_highPass_frequencyDomain(self):
        filterHighPass = get_filters("High pass", 8000, 70, 1500, None, 500)
        testSignal = ReadSignal(join(self.base_path, "Testcase 4/ecg400.txt"))
        expected_signal = ReadSignal(join(self.base_path, "Testcase 4/ecg_high_pass_filtered.txt"))

        filteredSignal = testSignal.apply_filter_in_frequency_domain(filterHighPass)
        self.assertTrue(CompSignals(filteredSignal, expected_signal, "Test case 4 (Frequency Domain)"))

    def test_bandPass_coefficients(self):
        filterBandPass = get_filters("Band Pass", 1000, 60, 150, 250, 50)
        expected_signal = ReadSignal(join(self.base_path, "Testcase 5/BPFCoefficients.txt"))
        self.assertTrue(CompSignals(filterBandPass, expected_signal, "Test case 5"))

    def test_bandPass_timeDomain(self):
        filterBandPass = get_filters("Band Pass", 1000, 60, 150, 250, 50)
        testSignal = ReadSignal(join(self.base_path, "Testcase 6/ecg400.txt"))
        expected_signal = ReadSignal(join(self.base_path, "Testcase 6/ecg_band_pass_filtered.txt"))

        filteredSignal = testSignal.convolve(filterBandPass)
        self.assertTrue(CompSignals(filteredSignal, expected_signal, "Test case 6 (Time Domain)"))

    def test_bandPass_frequencyDomain(self):
        filterBandPass = get_filters("Band Pass", 1000, 60, 150, 250, 50)
        testSignal = ReadSignal(join(self.base_path, "Testcase 6/ecg400.txt"))
        expected_signal = ReadSignal(join(self.base_path, "Testcase 6/ecg_band_pass_filtered.txt"))

        filteredSignal = testSignal.apply_filter_in_frequency_domain(filterBandPass)
        self.assertTrue(CompSignals(filteredSignal, expected_signal, "Test case 6 (Frequency Domain)"))

    def test_bandStop_coefficients(self):
        filterBandStop = get_filters("Band Stop", 1000, 60, 150, 250, 50)
        expected_signal = ReadSignal(join(self.base_path, "Testcase 7/BSFCoefficients.txt"))
        self.assertTrue(CompSignals(filterBandStop, expected_signal, "Test case 7"))

    def test_bandStop_timeDomain(self):
        filterBandStop = get_filters("Band Stop", 1000, 60, 150, 250, 50)
        testSignal = ReadSignal(join(self.base_path, "Testcase 8/ecg400.txt"))
        expected_signal = ReadSignal(join(self.base_path, "Testcase 8/ecg_band_stop_filtered.txt"))

        filteredSignal = testSignal.convolve(filterBandStop)
        self.assertTrue(CompSignals(filteredSignal, expected_signal, "Test case 8 (Time Domain)"))

    def test_bandStop_frequencyDomain(self):
        filterBandStop = get_filters("Band Stop", 1000, 60, 150, 250, 50)
        testSignal = ReadSignal(join(self.base_path, "Testcase 8/ecg400.txt"))
        expected_signal = ReadSignal(join(self.base_path, "Testcase 8/ecg_band_stop_filtered.txt"))

        filteredSignal = testSignal.apply_filter_in_frequency_domain(filterBandStop)
        self.assertTrue(CompSignals(filteredSignal, expected_signal, "Test case 8 (Frequency Domain)"))

