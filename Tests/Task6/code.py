from signal import signal

from TemplateMatchingClss import TemplateMatching
from TimeDelay import CalculateTimeDelay
from utilities import ReadSignal, CompSignals, ReadSignalValues
from Correlation import cross_correlation
from Signal import Signal


class Task6Test:
    def correlation_test(self):
        s1 = ReadSignal(file_path="Tests/Task6/CorrelationTest/input/Corr_input signal1.txt")
        s2 = ReadSignal(file_path="Tests/Task6/CorrelationTest/input/Corr_input signal2.txt")
        output = ReadSignal(file_path="Tests/Task6/CorrelationTest/output/CorrOutput.txt")

        correlation_result = cross_correlation(s1, s2)
        s3 = Signal(correlation_result)
        if CompSignals(s3, output, "correlation"):
            return "Test Correlation passed successfully"
        else:
            return "Test Correlation failed successfully"

    def TimeDelayTest(self):
        s1 = ReadSignal("Tests/Task6/TimeAnalysisTest/TD_input signal1.txt")
        s2 = ReadSignal("Tests/Task6/TimeAnalysisTest/TD_input signal2.txt")
        fs = 100
        res = CalculateTimeDelay(s1, s2, fs)
        if res == 5 / fs:
            return "Test TimeDelay passed successfully"
        else:
            return "Test TimeDelay failed successfully"

    def testTemplateMatching(self):
        s1 = ReadSignalValues("Tests/Task6/TemplateMatching/Test Signals/Test1.txt")
        s2 = ReadSignalValues("Tests/Task6/TemplateMatching/Test Signals/Test2.txt")

        tm = TemplateMatching()
        res =""
        res += f"signal1 --> {tm.classify(s1)}\n"
        res += f"\t\tsignal2 --> {tm.classify(s2)}"

        return res

    def Run(self):
        print("Task 6 Tests : ")
        print(50 * '-')
        print("\t" + "Correlation tests :")
        print("\t\t" + self.correlation_test())
        print("\t\t" + 50 * '-')
        print("\t" + "Time Delay tests :")
        print("\t\t" + self.TimeDelayTest())
        print("\t\t" + 50 * '-')
        print("\t" + "Template Matching tests :")
        print("\t\t" + self.testTemplateMatching())


