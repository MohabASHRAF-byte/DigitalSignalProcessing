from tkinter import ttk, filedialog
from Signal import Signal
from filters import get_filters
from tests.test_task3 import QuantizationTest
from utilities import ReadSignal


class TaskFilters(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.plot_frame = None
        self.signal_data = {}
        self.setup_gui()

    def setup_gui(self):
        ttk.Label(self, text="Filter Type:").grid(row=0, column=0, padx=5, pady=5)
        self.input_type = ttk.Combobox(self, values=["Low pass", "High pass", "Band Pass", "Band Stop"])
        self.input_type.grid(row=0, column=1, padx=5, pady=5)
        self.input_type.set("Filter Type")
        self.input_type.bind("<<ComboboxSelected>>", self.update_inputs)

        ttk.Label(self, text="Enter f1 Value (fc):").grid(row=1, column=0, padx=5, pady=5)
        self.f1_input = ttk.Entry(self)
        self.f1_input.grid(row=1, column=1, padx=5, pady=5)

        self.f2_label = ttk.Label(self, text="Enter f2 Value:")
        self.f2_input = ttk.Entry(self)

        self.fs_label = ttk.Label(self, text="fs:")
        self.fs_label.grid(row=2, column=0, padx=5, pady=5)
        self.fs_input = ttk.Entry(self)
        self.fs_input.grid(row=2, column=1, padx=5, pady=5)

        self.stop_band_attenuation_label = ttk.Label(self, text="Stop band attenuation:")
        self.stop_band_attenuation_label.grid(row=3, column=0, padx=5, pady=5)
        self.stop_band_attenuation_input = ttk.Entry(self)
        self.stop_band_attenuation_input.grid(row=3, column=1, padx=5, pady=5)

        # transition_band
        self.transition_band_label = ttk.Label(self, text="Transition band:")
        self.transition_band_label.grid(row=4, column=0, padx=5, pady=5)
        self.transition_band_input = ttk.Entry(self)
        self.transition_band_input.grid(row=4, column=1, padx=5, pady=5)

        open_signal_button = ttk.Button(self, text="Open File", command=self.open_file)
        open_signal_button.grid(row=6, column=0, padx=5, pady=10)
        self.open_signal_label = ttk.Label(self, text="No file uploaded")
        self.open_signal_label.grid(row=6, column=1, padx=5, pady=5)

        generate_button = ttk.Button(self, text="Apply filter", command=self.filter_signal)
        generate_button.grid(row=7, column=1, padx=5, pady=10)

    def update_inputs(self, event):
        selected_filter = self.input_type.get()

        if selected_filter in ["Low pass", "High pass"]:
            self.f2_label.grid_remove()
            self.f2_input.grid_remove()
        else:
            self.f2_label.grid(row=1, column=3, padx=5, pady=5)
            self.f2_input.grid(row=1, column=4, padx=5, pady=5)

    def filter_signal(self):
        filter_type = self.input_type.get()
        fs = int(self.fs_input.get())
        stop_band_attenuation = int(self.stop_band_attenuation_input.get())
        f1 = int(self.f1_input.get())
        if filter_type in ["Low pass", "High pass"]:
            f2 = None
        else:
            f2 = int(self.f2_input.get())
        transition_band = int(self.transition_band_input.get())

        generated_filter = get_filters(filter_type, fs, stop_band_attenuation, f1, f2, transition_band)
        filteredSignal = self.signal.convolve(generated_filter)
        self.export_filter(generated_filter, "filter")
        filteredSignal.plot_signal()
        print(filteredSignal)

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Select Signal File", filetypes=[("Text files", "*.txt")])
        self.signal = ReadSignal(file_path)
        self.open_signal_label.config(text="File uploaded")

    def export_filter(self, result: "Signal", title):
        file_path = filedialog.asksaveasfilename(
            title=f"Save {title}", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write("0\n")
                file.write("0\n")
                file.write(f"{len(result.data.items())}\n")
                for index, value in result.data.items():
                    file.write(f"{index} {value}\n")