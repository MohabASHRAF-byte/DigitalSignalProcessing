from tkinter import ttk, filedialog
from tkinter import messagebox
from Functions.Correlation import cross_correlation
from Signal import Signal
from utilities import ReadSignal


class TaskCorrelation(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.plot_frame = None
        self.signal_data = {}
        self.setup_gui()

    def setup_gui(self):
        open_signal_button = ttk.Button(
            self, text="Open File", command=self.open_first_signal
        )
        open_signal_button.grid(row=1, column=0, padx=5, pady=10)
        self.open_signal_label = ttk.Label(self, text="No file uploaded")
        self.open_signal_label.grid(row=1, column=1, padx=5, pady=5)

        open_second_signal_button = ttk.Button(
            self, text="Open File", command=self.open_second_signal
        )
        open_second_signal_button.grid(row=2, column=0, padx=5, pady=10)
        self.open_second_signal_label = \
            ttk.Label(self, text="No file uploaded")
        self.open_second_signal_label.grid(row=2, column=1, padx=5, pady=5)

        generate_button = ttk.Button(
            self, text="Correlate", command=self.correlate
        )
        generate_button.grid(row=7, column=1, padx=5, pady=10)

    def open_first_signal(self):
        file_path = filedialog.askopenfilename(
            title="Select First Signal File",
            filetypes=[("Text files", "*.txt")]
        )
        self.first_signal = ReadSignal(file_path)
        self.open_signal_label.config(text="File uploaded")

    def open_second_signal(self):
        file_path = filedialog.askopenfilename(
            title="Select Second Signal File",
            filetypes=[("Text files", "*.txt")]
        )
        self.second_signal = ReadSignal(file_path)
        self.open_second_signal_label.config(text="File uploaded")

    def correlate(self):
        if not self.first_signal or not self.second_signal:
            messagebox.showinfo("Error", "Upload the two signals first")
        result = cross_correlation(self.first_signal, self.second_signal)
        result = Signal(result)
        result.plot_signal()
