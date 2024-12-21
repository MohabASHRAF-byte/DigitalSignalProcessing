from tests.test_task1 import Task1Test
from tests.test_task3 import QuantizationTest
from tests.test_task4 import Task4Test
from tests.test_task5 import Task5Test
from tests.test_task6 import Task6Test
from tests.test_filters import PracticalFiltersTest

class RunAllTests:
    @staticmethod
    def Run():
        tests =[
            Task1Test() ,
            QuantizationTest() ,
            Task4Test() ,
            Task5Test() ,
            Task6Test(),
            # PracticalFiltersTest()
        ]
        for test in tests:
            test.Run()
            print("*"* 100 )
