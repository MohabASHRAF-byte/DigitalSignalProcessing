from tkinter import ttk, filedialog
import numpy as np
import  math

class Task3(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.plot_frame = None
        self.signal_data = {}
        self.setup_gui()

    def setup_gui(self):
        ttk.Label(self, text="Select Input Type:").grid(row=0, column=0, padx=5, pady=5)
        self.input_type = ttk.Combobox(self, values=["Levels", "Bits"])
        self.input_type.grid(row=0, column=1, padx=5, pady=5)
        self.input_type.set("Select Input Type")

        ttk.Label(self, text="Enter Value:").grid(row=1, column=0, padx=5, pady=5)
        self.value_entry = ttk.Entry(self)
        self.value_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="Select test:").grid(row=2, column=0, padx=5, pady=5)
        self.test_value = ttk.Combobox(self, values=["test-1", "test-2"])
        self.test_value.grid(row=2, column=1, padx=5, pady=5)
        self.test_value.set("Select test")

        open_file_button = ttk.Button(self, text="Open File", command=self.open_file)
        open_file_button.grid(row=3, column=0, padx=5, pady=10)

        generate_button = ttk.Button(self, text="Quantize Signal", command=self.quantize_signal)
        generate_button.grid(row=3, column=1, padx=5, pady=10)

    def open_file(self):
        """Open a file and read a single signal from it."""
        file_path = filedialog.askopenfilename(title="Select Text File", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                self.signal_data = {}  # Clear previous data
                for line in file:
                    parts = line.strip().split()
                    if len(parts) == 2:
                        index = int(parts[0])
                        value = float(parts[1])
                        self.signal_data[index] = value
            print("Signal Data Loaded:", self.signal_data)

    def quantize_signal(self):
        """Perform signal quantization based on input type and value."""
        if not self.signal_data:
            print("No signal data available.")
            return

        test_numbers = self.test_value.get()
        input_type = self.input_type.get()
        value = int(self.value_entry.get())
        data = np.array(list(self.signal_data.values()))

        minE = min(data)
        maxE = max(data)

        if input_type == "Levels":
            levels = value
        elif input_type == "Bits":
            levels = 2 ** value
        else:
            print("Invalid input type selected.")
            return

        len = int(math.log2(levels))
        delta = (maxE - minE) / levels
        lvls = [minE + delta / 2]
        lv = [bin(num)[2:].zfill(len) for num in range(levels)]
        for i in range(levels - 1):
            lvls.append(lvls[-1] + delta)

        output = []
        intervalIndices = []
        encodedValues = []
        quantizedValues = []
        sampledError = []
        for point in data:
            err = int(1e15)
            x = 0
            for i in range(levels):
                if round(abs(point - lvls[i]), 2) < err:
                    x = i
                    err = round(abs(point - lvls[i]), 2)
                output.append([x + 1, lv[x], round(lvls[x], 3), round(lvls[x] - point, 3)])
            intervalIndices.append(x + 1)
            encodedValues.append(lv[x])
            quantizedValues.append(round(lvls[x], 3))
            sampledError.append(round(lvls[x] - point, 3))
            output.append([x + 1, lv[x], round(lvls[x], 3), round(lvls[x] - point, 3)])

        for i in output:
            print(i)

        if test_numbers == "test-1":
            self.QuantizationTest1("Task3Test1Out.txt", encodedValues, quantizedValues)
        elif test_numbers == "test-2":
            self.QuantizationTest2("Task3Test2Out.txt", intervalIndices, encodedValues, quantizedValues, sampledError)


    def QuantizationTest1(self, file_name, Your_EncodedValues, Your_QuantizedValues):
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

    def QuantizationTest2(self, file_name, Your_IntervalIndices, Your_EncodedValues, Your_QuantizedValues, Your_SampledError):
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