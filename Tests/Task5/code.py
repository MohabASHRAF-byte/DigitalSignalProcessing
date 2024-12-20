from signal import signal
import math

from utilities import ReadSignal, CompSignals, ReadSignalInFrequencyDomain, SignalCompareAmplitude, \
    SignalComparePhaseShift


class Task5Test:
    def dftTest1(self):
        in_signal = ReadSignal("Tests/Task5/DFT/input_Signal_DFT.txt")
        out_signal = ReadSignalInFrequencyDomain("Tests/Task5/DFT/Output_Signal_DFT.txt")

        in_signal.dft(8)

        CompAmpResult = SignalCompareAmplitude(in_signal, out_signal)
        CompShiftResult = SignalComparePhaseShift(in_signal, out_signal)
        if CompAmpResult and CompShiftResult:
            return "Test DFT passed successfully"
        else:
            return "Test DFT failed successfully"

    def idftTest1(self):
        in_signal = ReadSignalInFrequencyDomain("Tests/Task5/IDFT/Input_Signal_IDFT.txt")
        out_signal = ReadSignal("Tests/Task5/IDFT/Output_Signal_IDFT.txt")

        in_signal.idft(8)


        comp = CompSignals(in_signal, out_signal, "")
        if comp:
            return "Test IDFT passed successfully"
        else:
            return "Test IDFT failed successfully"

    def RunAllTests(self):
        print("Task 5 Tests : ")
        print(50 * '-')
        print("\t" + "DFT tests :")
        print("\t\t" + self.dftTest1())
        print("\t" + 25 * '-')
        print("\t" + "IDFT tests : ")
        print("\t\t" + self.idftTest1())
        print("*"*100)
