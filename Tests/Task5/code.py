from signal import signal
import math

from utilities import ReadSignal, CompSignals

class Task5Test:
    def dftTest1(self):
        in_signal = ReadSignal("Tests/Task5/DFT/input_Signal_DFT.txt")
        dftSignal = [round(value, 15) for value in in_signal.dft(10).get_signal_values()]
        out_signal = ReadSignal("Tests/Task5/DFT/Output_Signal_DFT.txt", True)
        if self.SignalComapreAmplitude(dftSignal, out_signal.get_signal_values()) and self.SignalComaprePhaseShift(dftSignal, out_signal.get_signal_values()):
            return "Test DFT passed successfully"
        else:
            return "Test DFT failed successfully"

    def idftTest1(self):
        in_signal = ReadSignal("Tests/Task5/IDFT/Input_Signal_IDFT.txt", True)
        dftSignal = in_signal.idft(10)
        # print(in_signal.originalData)
        print(dftSignal.get_signal_values())
        out_signal = ReadSignal("Tests/Task5/IDFT/Output_Signal_IDFT.txt")
        print("-----------")
        # print(out_signal.get_signal_values())
        if self.SignalComapreAmplitude(dftSignal.get_signal_values(), out_signal.get_signal_values()):
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
        print("\t" + 25 * '-')

    def SignalComapreAmplitude(self, SignalInput = [] ,SignalOutput= []):
        if len(SignalInput) != len(SignalOutput):
            return False
        else:
            for i in range(len(SignalInput)):
                if abs(SignalInput[i]-SignalOutput[i])>0.001:
                    return False
            return True

    def SignalComaprePhaseShift(self, SignalInput=[], SignalOutput=[]):
        if len(SignalInput) != len(SignalOutput):
            return False
        else:
            for i in range(len(SignalInput)):
                A = round(SignalInput[i])
                B = round(SignalOutput[i])
                if abs(A - B) > 0.0001:
                    return False
                elif A != B:
                    return False
            return True