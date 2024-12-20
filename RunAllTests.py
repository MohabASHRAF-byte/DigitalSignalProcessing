from Tests.Practical.code import PracticalFiltersTest
from Tests.Task1.code import Task1Test
from Tests.Task3.code import QuantizationTest
from Tests.Task4.code import Task4
from Tests.Task5.code import Task5Test
from Tests.Task6.code import Task6Test


class RunAllTests:
    @staticmethod
    def Run():
        tests =[
            Task1Test() ,
            QuantizationTest() ,
            Task4() ,
            Task5Test() ,
            Task6Test(),
            PracticalFiltersTest()
        ]
        for test in tests:
            test.Run()
            print("*"* 100 )
