import utilities
from Signal import Signal
class QuantizationTest : 
    def __init__(self):
        self.inputFilePath=[f"Tests/Task3/Test1/in.txt",f"Tests/Task3/Test2/in.txt"]
        self.outputFilePath=[f"Tests/Task3/Test1/out.txt",f"Tests/Task3/Test2/out.txt"]
    def GetTestSignal( self, index : int):
        index  -= 1
        if index >= len(self.inputFilePath):
            return -1
        filePath = self.inputFilePath[index]
        return utilities.ReadSignal(filePath)
    def GetTestOutputPath( self, index : int):
        index  -= 1
        if index >= len(self.outputFilePath):
            return -1
        return self.outputFilePath[index]
   
    def Test1(self,signal:Signal):
            Your_EncodedValues = signal.encoded_values
            Your_QuantizedValues = signal.quantized_values
            file_name=self.outputFilePath[0]
            expectedEncodedValues = []
            expectedQuantizedValues = []
            with open(file_name, 'r') as f:
                line = f.readline()
                line = f.readline()
                line = f.readline()
                line = f.readline()
                while line:
                    # process line
                    L = line.strip()
                    if len(L.split(' ')) == 2:
                        L = line.split(' ')
                        V2 = str(L[0])
                        V3 = float(L[1])
                        expectedEncodedValues.append(V2)
                        expectedQuantizedValues.append(V3)
                        line = f.readline()
                    else:
                        break
            if ((len(Your_EncodedValues) != len(expectedEncodedValues)) or (
                    len(Your_QuantizedValues) != len(expectedQuantizedValues))):
                print("QuantizationTest1 Test case failed, your signal have different length from the expected one")
                return
            for i in range(len(Your_EncodedValues)):
                if (Your_EncodedValues[i] != expectedEncodedValues[i]):
                    print(
                        "QuantizationTest1 Test case failed, your EncodedValues have different EncodedValues from the expected one")
                    return
            for i in range(len(expectedQuantizedValues)):
                if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
                    continue
                else:
                    print(
                        "QuantizationTest1 Test case failed, your QuantizedValues have different values from the expected one")
                    return
            print("QuantizationTest1 Test case passed successfully")
    
    def Test2(self,signal:Signal):
        Your_IntervalIndices = signal.interval_indices
        Your_EncodedValues = signal.encoded_values
        Your_QuantizedValues =signal.quantized_values
        Your_SampledError = signal.errors
        file_name = self.outputFilePath[1]
        expectedIntervalIndices = []
        expectedEncodedValues = []
        expectedQuantizedValues = []
        expectedSampledError = []
        with open(file_name, 'r') as f:
            line = f.readline()
            line = f.readline()
            line = f.readline()
            line = f.readline()
            while line:
                # process line
                L = line.strip()
                if len(L.split(' ')) == 4:
                    L = line.split(' ')
                    V1 = int(L[0])
                    V2 = str(L[1])
                    V3 = float(L[2])
                    V4 = float(L[3])
                    expectedIntervalIndices.append(V1)
                    expectedEncodedValues.append(V2)
                    expectedQuantizedValues.append(V3)
                    expectedSampledError.append(V4)
                    line = f.readline()
                else:
                    break
        if (len(Your_IntervalIndices) != len(expectedIntervalIndices)
                or len(Your_EncodedValues) != len(expectedEncodedValues)
                or len(Your_QuantizedValues) != len(expectedQuantizedValues)
                or len(Your_SampledError) != len(expectedSampledError)):
            print("QuantizationTest2 Test case failed, your signal have different length from the expected one")
            return
        
        for i in range(len(Your_IntervalIndices)):
            if (Your_IntervalIndices[i] != expectedIntervalIndices[i]):
                print("QuantizationTest2 Test case failed, your signal have different indicies from the expected one")
                return
        for i in range(len(Your_EncodedValues)):
            if (Your_EncodedValues[i] != expectedEncodedValues[i]):
                print(
                    "QuantizationTest2 Test case failed, your EncodedValues have different EncodedValues from the expected one")
                return

        for i in range(len(expectedQuantizedValues)):
            if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
                continue
            else:
                print(
                    "QuantizationTest2 Test case failed, your QuantizedValues have different values from the expected one")
                return
        for i in range(len(expectedSampledError)):
            if abs(Your_SampledError[i] - expectedSampledError[i]) < 0.01:
                continue
            else:
                print(
                    "QuantizationTest2 Test case failed, your SampledError have different values from the expected one")
                return
        print("QuantizationTest2 Test case passed successfully")
    def Run(self):
        print("Run Task 3 Tests")
        print(".......................")
        signal1 = self.GetTestSignal(1)
        signal1.quantize_signal(level=8)
        signal2 = self.GetTestSignal(2)
        signal2.quantize_signal(level=4)
        Tester = QuantizationTest()
        Tester.Test1(signal=signal1)
        Tester.Test2(signal=signal2)


