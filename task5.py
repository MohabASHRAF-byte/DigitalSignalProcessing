from tkinter import ttk, filedialog
from Signal import Signal
from Tests.Task3.code import QuantizationTest
from utilities import ReadSignal

class Task5(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.signal_data = None
        self.setup_gui()

    def setup_gui(self):
        # Sampling frequency input
        ttk.Label(self, text="Enter Sampling Frequency (Hz):").grid(row=0, column=0, padx=5, pady=5)
        self.sampling_frequency_entry = ttk.Entry(self)
        self.sampling_frequency_entry.grid(row=0, column=1, padx=5, pady=5)

        # Button to open file
        open_file_button = ttk.Button(self, text="Open File", command=self.open_file)
        open_file_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Button to call Fourier Transform
        fourier_button = ttk.Button(self, text="Apply Fourier Transform", command=self.apply_fourier_transform)
        fourier_button.grid(row=2, column=0, columnspan=2, pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Select Text File", filetypes=[("Text files", "*.txt")])
        self.signal_data = ReadSignal(file_path)

    def apply_fourier_transform(self):
        """Apply the Fourier Transform and display the results."""
        if not self.signal_data:
            print("No signal data loaded.")
            return

        try:
            sampling_frequency = float(self.sampling_frequency_entry.get())
            if sampling_frequency <= 0:
                raise ValueError("Sampling frequency must be positive.")

            # Fourier Transform logic (implement the DFT in the Signal class)
            self.signal_data.dft(sampling_frequency)
            print("Fourier Transform applied successfully.")
        except ValueError as e:
            print(f"Invalid input: {e}")