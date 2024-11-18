from main import setup_gui
from test import test
from Tests.Task1.code import Task1Test
from Tests.Task3.code import QuantizationTest
from Tests.Task4.code import Task4
class RunAllTests:
    @staticmethod
    def Run():
        ob = Task1Test()
        ob.Task1TestRunner()
        ob2 = QuantizationTest()
        ob2.RunAllTests()
        ob3 = Task4()
        ob3.RunAllTests()