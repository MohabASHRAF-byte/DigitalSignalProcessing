from Tests.Practical.filters import get_filters
from utilities import ReadSignal, CompSignals


class PracticalFiltersTest:
    def lowPassTest(self):
        filterLowPass = get_filters("Low pass", 8000, 50, 1500, None, 500)
        expected_signal = ReadSignal("./Tests/Practical/FIR test cases/Testcase 1/LPFCoefficients.txt")
        print(CompSignals(filterLowPass, expected_signal, "\tTest case 1:"))

        testSignal = ReadSignal("./Tests/Practical/FIR test cases/Testcase 2/ecg400.txt")
        expected_signal = ReadSignal("./Tests/Practical/FIR test cases/Testcase 2/ecg_low_pass_filtered.txt")

        filteredSignal = testSignal.convolve(filterLowPass)
        print(CompSignals(filteredSignal, expected_signal, "\tTest case 2 (Time Domain):"))

        filteredSignal = testSignal.apply_filter_in_frequency_domain(filterLowPass)
        print(CompSignals(filteredSignal, expected_signal, "\tTest case 2 (Frequency Domain):"))

    def highPassTest(self):
        filterHighPass = get_filters("High pass", 8000, 70, 1500, None, 500)

        expected_signal = ReadSignal("./Tests/Practical/FIR test cases/Testcase 3/HPFCoefficients.txt")
        print(CompSignals(filterHighPass, expected_signal, "\tTest case 3:"))

        testSignal = ReadSignal("./Tests/Practical/FIR test cases/Testcase 4/ecg400.txt")
        expected_signal = ReadSignal("./Tests/Practical/FIR test cases/Testcase 4/ecg_high_pass_filtered.txt")

        filteredSignal = testSignal.convolve(filterHighPass)
        print(CompSignals(filteredSignal, expected_signal, "\tTest case 4 (Time Domain):"))

        filteredSignal = testSignal.apply_filter_in_frequency_domain(filterHighPass)
        print(CompSignals(filteredSignal, expected_signal, "\tTest case 4 (Frequency Domain):"))

    def bandPassTest(self):
        filterBandPass = get_filters("Band Pass", 1000, 60, 150, 250, 50)

        expected_signal = ReadSignal("./Tests/Practical/FIR test cases/Testcase 5/BPFCoefficients.txt")
        print(CompSignals(filterBandPass, expected_signal, "\tTest case 5:"))

        testSignal = ReadSignal("./Tests/Practical/FIR test cases/Testcase 6/ecg400.txt")
        expected_signal = ReadSignal("./Tests/Practical/FIR test cases/Testcase 6/ecg_band_pass_filtered.txt")

        filteredSignal = testSignal.convolve(filterBandPass)
        print(CompSignals(filteredSignal, expected_signal, "\tTest case 6 (Time Domain):"))

        filteredSignal = testSignal.apply_filter_in_frequency_domain(filterBandPass)
        print(CompSignals(filteredSignal, expected_signal, "\tTest case 6 (Frequency Domain):"))

    def bandStopTest(self):
        filterBandStop = get_filters("Band Stop", 1000, 60, 150, 250, 50)

        expected_signal = ReadSignal("./Tests/Practical/FIR test cases/Testcase 7/BSFCoefficients.txt")
        print(CompSignals(filterBandStop, expected_signal, "\tTest case 7:"))

        testSignal = ReadSignal("./Tests/Practical/FIR test cases/Testcase 8/ecg400.txt")
        expected_signal = ReadSignal("./Tests/Practical/FIR test cases/Testcase 8/ecg_band_stop_filtered.txt")

        filteredSignal = testSignal.convolve(filterBandStop)
        print(CompSignals(filteredSignal, expected_signal, "\tTest case 8 (Time Domain):"))

        filteredSignal = testSignal.apply_filter_in_frequency_domain(filterBandStop)
        print(CompSignals(filteredSignal, expected_signal, "\tTest case 8 (Frequency Domain):"))

    def RunAllTests(self):
        print("Practical Filters Tests : ")
        print(50 * '-')
        print("\t" + "Low Pass Filter")
        self.lowPassTest()
        print("\t" + 25 * '-')
        print("\t" + "Hight Pass Filter")
        self.highPassTest()
        print("\t" + 25 * '-')
        print("\t" + "Band Pass Filter")
        self.bandPassTest()
        print("\t" + 25 * '-')
        print("\t" + "Band Stop Filter")
        self.bandStopTest()
