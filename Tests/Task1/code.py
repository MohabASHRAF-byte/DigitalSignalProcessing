from utilities import ReadSignal
def check_signal(signal3 ,Expected ,Message):
        Your_indices,Your_samples = signal3.get_signal_indexs(),signal3.get_signal_values()
        expected_indices,expected_samples=Expected.get_signal_indexs(),Expected.get_signal_values()          
        if (len(expected_samples)!=len(Your_samples)) and (len(expected_indices)!=len(Your_indices)):
             return Message+" Test case failed, your signal have different length from the expected one"
    
        for i in range(len(Your_indices)):
            if(Your_indices[i]!=expected_indices[i]):
                return Message + " Test case failed, your signal have different indicies from the expected one"
        for i in range(len(expected_samples)):
            if abs(Your_samples[i] - expected_samples[i]) < 0.01:
                continue
            else:
                return Message +" Test case failed, your signal have different values from the expected one"
             
        return Message +" Test case passed successfully"
    
class Task1Test:
    def AddationTest (self):
        signal1 = ReadSignal("Tests/Task1/Signal1.txt")
        signal2 = ReadSignal("Tests/Task1/Signal2.txt")
        signal3 = signal1 + signal2
        addSignal = ReadSignal("Tests/Task1/add.txt")
        print(check_signal(signal3,addSignal,"Addation"))
        
    def SubtractiaonTest (self):
        signal1 = ReadSignal("Tests/Task1/Signal1.txt")
        signal2 = ReadSignal("Tests/Task1/Signal2.txt")
        signal3 = signal1 - signal2
        SubSignal = ReadSignal("Tests/Task1/subtract.txt")
        result = check_signal(signal3 , SubSignal , "Subtraction")
        print(result)

    def MulTest(self):
        signal1 = ReadSignal("Tests/Task1/Signal1.txt")
        signal3 = signal1 * 5
        mulBy5Signal = ReadSignal("Tests/Task1/mul5.txt")
        result = check_signal(signal3 , mulBy5Signal , "Mul5")
        print(result)

    def AdavnceTest(self):
        signal1 = ReadSignal("Tests/Task1/Signal1.txt")
        advance5 = ReadSignal("Tests/Task1/advance3.txt")
        signal1.DelayingOrAdvancingSignalByK(-3)
        result = check_signal(signal1,advance5,"Advacning By 5 ")
        print(result)

    def DelayTest(self):
        signal1 = ReadSignal("Tests/Task1/Signal1.txt")
        delay5 = ReadSignal("Tests/Task1/delay3.txt")
        signal1.DelayingOrAdvancingSignalByK(3)
        result = check_signal(signal1,delay5,"Delay By 5 ")
        print(result)
    
    def FoldingTest(self):
        signal1 = ReadSignal("Tests/Task1/Signal1.txt")
        mirror = ReadSignal("Tests/Task1/folding.txt")
        signal1.mirror()
        result = check_signal(signal1,mirror,"Folding")
        print(result)

    def Task1TestRunner(self):
        print("Run Task 1 Tests ")
        print(".......................")
        self.AddationTest()
        self.SubtractiaonTest()
        self.MulTest()
        self.AdavnceTest()
        self.DelayTest()
        self.FoldingTest()
        print("*"*50)
