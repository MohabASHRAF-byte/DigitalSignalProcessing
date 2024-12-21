from tests.test_task3 import QuantizationTest


class RunAllTests:
    @staticmethod
    def Run():
        tests =[
            # Task1Test() ,
            QuantizationTest() ,
            # Task4Test() ,
            # Task5Test() ,
            # Task6Test(),
            # PracticalFiltersTest()
        ]
        for test in tests:
            test.Run()
            print("*"* 100 )
