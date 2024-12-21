from tkinter import ttk
from tests.test_task3 import QuantizationTest


class Task3(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.plot_frame = None
        self.signal_data = {}
        self.setup_gui()

    def setup_gui(self):
        (ttk.Label(self, text="Select Input Type:")
         .grid(row=0, column=0, padx=5, pady=5))
        self.input_type = ttk.Combobox(self, values=["Levels", "Bits"])
        self.input_type.grid(row=0, column=1, padx=5, pady=5)
        self.input_type.set("Select Input Type")

        (ttk.Label(self, text="Enter Value:")
         .grid(row=1, column=0, padx=5, pady=5))
        self.value_entry = ttk.Entry(self)
        self.value_entry.grid(row=1, column=1, padx=5, pady=5)

        (ttk.Label(self, text="Select test:")
         .grid(row=2, column=0, padx=5, pady=5))
        self.test_value = ttk.Combobox(self, values=["test-1", "test-2"])
        self.test_value.grid(row=2, column=1, padx=5, pady=5)
        self.test_value.set("Select test")

        # open_file_button = ttk.Button(self, text="Open File", command=Read())
        # open_file_button.grid(row=3, column=0, padx=5, pady=10)

        generate_button = ttk.Button(self,
                                     text="Quantize Signal",
                                     command=self.quantize_signal
                                     )
        generate_button.grid(row=3, column=1, padx=5, pady=10)

    def quantize_signal(self):
        """
        Perform signal quantization based on input type and value.
        """

        Tester = QuantizationTest()
        Tester.Run()
        if self.test_value.get() == "test-1":
            testNumber = 1
        elif self.test_value.get() == "test-2":
            testNumber = 2

        # Read the input file using relative path
        signal = Tester.GetTestSignal(testNumber)

        if signal is None:
            print("No signal data available.")
            return

        # Get the Levels
        LevelsOrBits = self.input_type.get()
        value = int(self.value_entry.get())

        # Set up perception
        perception = 2 if not testNumber == 2 else 3

        #  call quantaize the signal
        if LevelsOrBits == "Levels":
            signal.quantize_signal(level=value, perception=perception)
        if LevelsOrBits == "Bits":
            signal.quantize_signal(bits=value, perception=perception)

        #  Run the testing
        if testNumber == 1:
            Tester.test_Test1()
        else:
            Tester.test_Test2()
