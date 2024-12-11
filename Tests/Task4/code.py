from signal import signal

from utilities import ReadSignal, CompSignals


class Task4:
    def Move_Avg_test1(self):
        in_signal = ReadSignal("Tests/Task4/Moving_Average/MovingAvg_input.txt")
        in_signal.Average(window_size=3, perception=3)
        out_signal = ReadSignal("Tests/Task4/Moving_Average/MovingAvg_out1.txt")
        result = CompSignals(in_signal, out_signal, "Moving Average Window = 3 --> ")
        return result

    def Move_Avg_test2(self):
        in_signal = ReadSignal("Tests/Task4/Moving_Average/MovingAvg_input.txt")
        in_signal.Average(window_size=5, perception=1)
        out_signal = ReadSignal("Tests/Task4/Moving_Average/MovingAvg_out2.txt")
        result = CompSignals(in_signal, out_signal, "Moving Average Window = 5 --> ")
        return result

    def Derivative_test1(self):
        in_signal = ReadSignal("Tests/Task4/Derivative/Derivative_input.txt")
        out_signal = ReadSignal("Tests/Task4/Derivative/1st_derivative_out.txt")
        in_signal.derivative(1)
        result = CompSignals(in_signal, out_signal, "1st Derivative")
        return result

    def Derivative_test2(self):
        in_signal = ReadSignal("Tests/Task4/Derivative/Derivative_input.txt")
        out_signal = ReadSignal("Tests/Task4/Derivative/2nd_derivative_out.txt")
        in_signal.derivative(2)
        result = CompSignals(in_signal, out_signal, "2st Derivative")
        return result

    def Convolution_test(self):
        in_signal1 = ReadSignal("Tests/Task4/Convolution/Signal 1.txt")
        in_signal2 = ReadSignal("Tests/Task4/Convolution/Signal 2.txt")
        out_signal = ReadSignal("Tests/Task4/Convolution/Conv_output.txt")
        out2 = in_signal1.convolve(in_signal2)
        result = CompSignals(out2, out_signal, "Convolution")
        return result

    def RunAllTests(self):
        print("Task 4 Tests : ")
        print(50 * '-')
        print("\t" + "Avg tests :")
        print("\t\t" + self.Move_Avg_test1())
        print("\t\t" + self.Move_Avg_test2())
        print("\t" + 25 * '-')

        print("\t" + "Derivative tests : ")
        print("\t\t" + self.Derivative_test1())
        print("\t\t" + self.Derivative_test2())
        print("\t" + 25 * '-')

        print("\t" + "Convolution tests : ")
        print("\t\t" + self.Convolution_test())
        print("*"*100)
