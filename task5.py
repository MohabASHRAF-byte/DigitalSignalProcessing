import tkinter as tk
from tkinter import simpledialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from math import pi, sin, cos, sqrt, atan2
from Signal import Signal
# Assuming the Signal class you provided is imported here
# from signal_class import Signal  # Replace this with your actual import

class SignalVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Signal Fourier Transform Visualizer")

        # GUI Elements
        self.label_intro = tk.Label(root, text="Enter Signal Values (index:value) Separated by Commas:")
        self.label_intro.pack(pady=5)

        self.entry_signal = tk.Entry(root, width=60)
        self.entry_signal.pack(pady=5)

        self.label_fs = tk.Label(root, text="Enter Sampling Frequency (Hz):")
        self.label_fs.pack(pady=5)

        self.entry_fs = tk.Entry(root, width=20)
        self.entry_fs.pack(pady=5)

        self.btn_process = tk.Button(root, text="Perform Fourier Transform", command=self.process_signal)
        self.btn_process.pack(pady=10)

        # Canvas placeholders for plots
        self.canvas_amplitude = None
        self.canvas_phase = None

    def process_signal(self):
        try:
            # Parse signal input
            signal_input = self.entry_signal.get().strip()
            if not signal_input:
                raise ValueError("Signal input cannot be empty.")

            signal_dict = {}
            for pair in signal_input.split(","):
                key, value = map(float, pair.strip().split(":"))
                signal_dict[int(key)] = float(value)

            # Parse sampling frequency
            fs = int(self.entry_fs.get().strip())
            if fs <= 0:
                raise ValueError("Sampling frequency must be a positive integer.")

            # Initialize the Signal object and perform DFT
            signal = Signal(signal_dict)
            amplitudes, phases = signal.dft(fs)

            # Plot Frequency vs Amplitude and Frequency vs Phase
            self.plot_results(amplitudes, phases, fs)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def plot_results(self, amplitudes, phases, fs):
        # Clear previous plots
        if self.canvas_amplitude:
            self.canvas_amplitude.get_tk_widget().destroy()
        if self.canvas_phase:
            self.canvas_phase.get_tk_widget().destroy()

        # Generate frequency axis
        freq_axis = [i for i in range(len(amplitudes))]

        # Plot Amplitude Spectrum as a column chart
        fig1, ax1 = plt.subplots()
        ax1.bar(freq_axis, amplitudes, color='b')
        ax1.set_title("Frequency vs Amplitude")
        ax1.set_xlabel("Frequency (Hz)")
        ax1.set_ylabel("Amplitude")
        ax1.grid()

        self.canvas_amplitude = FigureCanvasTkAgg(fig1, master=self.root)
        self.canvas_amplitude.draw()
        self.canvas_amplitude.get_tk_widget().pack(pady=10)

        # Plot Phase Spectrum as a column chart
        fig2, ax2 = plt.subplots()
        ax2.bar(freq_axis, phases, color='r')
        ax2.set_title("Frequency vs Phase")
        ax2.set_xlabel("Frequency (Hz)")
        ax2.set_ylabel("Phase (Radians)")
        ax2.grid()

        self.canvas_phase = FigureCanvasTkAgg(fig2, master=self.root)
        self.canvas_phase.draw()
        self.canvas_phase.get_tk_widget().pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = SignalVisualizer(root)
    root.mainloop()