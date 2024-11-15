from main import setup_gui
from test import test
from Tests.Task1.code import Task1Test
from Tests.Task3.code import QuantizationTest

class RunAllTests:
    @staticmethod
    def Run():
        ob = Task1Test()
        ob.Task1TestRunner()
        ob2 = QuantizationTest()
        ob2.RunAllTests()