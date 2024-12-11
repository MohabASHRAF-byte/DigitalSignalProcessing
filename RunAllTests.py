
from Tests.Task1.code import Task1Test
from Tests.Task3.code import QuantizationTest
from Tests.Task4.code import Task4
from Tests.Task5.code import Task5Test

class RunAllTests:
    @staticmethod
    def Run():
        ob = Task1Test()
        ob.Task1TestRunner()
        ob2 = QuantizationTest()
        ob2.RunAllTests()
        ob3 = Task4()
        ob3.RunAllTests()
        ob4 = Task5Test()
        ob4.RunAllTests()
