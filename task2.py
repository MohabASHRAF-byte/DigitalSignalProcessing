from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Task2(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.plot_frame = None
        self.setup_gui()

    def setup_gui(self):
        # Create and organize input widgets for Task 2
        ttk.Label(self, text="Amplitude:").grid(row=0, column=0, padx=5, pady=5)
        self.amplitude_entry = ttk.Entry(self)
        self.amplitude_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Theta (degrees):").grid(row=1, column=0, padx=5, pady=5)
        self.theta_entry = ttk.Entry(self)
        self.theta_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="Frequency (Hz):").grid(row=2, column=0, padx=5, pady=5)
        self.frequency_entry = ttk.Entry(self)
        self.frequency_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self, text="Sampling Frequency (Hz):").grid(row=3, column=0, padx=5, pady=5)
        self.fs_entry = ttk.Entry(self)
        self.fs_entry.grid(row=3, column=1, padx=5, pady=5)

        # Dropdown for selecting wave type (Sine or Cosine)
        self.wave_type = ttk.Combobox(self, values=["Sine Wave", "Cosine Wave"])
        self.wave_type.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.wave_type.set("Select Wave Type")

        # Dropdown for selecting plot type (Discrete, Continuous, or Both)
        self.plot_type = ttk.Combobox(self, values=["Discrete", "Continuous", "Both"])
        self.plot_type.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        self.plot_type.set("Select Plot Type")

        # Button to generate the signal
        generate_button = ttk.Button(self, text="Generate Signal", command=self.generate_signal)
        generate_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

        # Frame for displaying the plot
        self.plot_frame = ttk.Frame(self, borderwidth=2, relief="solid")
        self.plot_frame.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    def generate_signal(self):
        try:
            amplitude = float(self.amplitude_entry.get())
            theta = np.radians(float(self.theta_entry.get()))  # Convert degrees to radians
            frequency = float(self.frequency_entry.get())
            fs = float(self.fs_entry.get())

            # Time array for both continuous and discrete signals
            t_continuous = np.linspace(0, 4, 1000)  # Fine sampling for continuous signal
            t_discrete = np.arange(0, 4, 1/fs)  # Discrete time steps based on fs

            # Generate the signal based on the selected wave type
            if self.wave_type.get() == "Sine Wave":
                continuous_signal = amplitude * np.sin(2 * np.pi * frequency * t_continuous + theta)
                discrete_signal = amplitude * np.sin(2 * np.pi * frequency * t_discrete + theta)
            elif self.wave_type.get() == "Cosine Wave":
                continuous_signal = amplitude * np.cos(2 * np.pi * frequency * t_continuous + theta)
                discrete_signal = amplitude * np.cos(2 * np.pi * frequency * t_discrete + theta)
            else:
                raise ValueError("Invalid wave type selected")

            self.plot_generated_signal(t_continuous, continuous_signal, t_discrete, discrete_signal)

        except ValueError as e:
            print(f"Error: {e}")

    def plot_generated_signal(self, t_continuous, continuous_signal, t_discrete, discrete_signal):
        fig, ax = plt.subplots(figsize=(8, 3))

        # Determine which plot types to show (discrete, continuous, or both)
        plot_type = self.plot_type.get()
        if plot_type == "Discrete":
            ax.stem(t_discrete, discrete_signal, use_line_collection=True, label="Discrete")
        elif plot_type == "Continuous":
            ax.plot(t_continuous, continuous_signal, label="Continuous")
        elif plot_type == "Both":
            ax.plot(t_continuous, continuous_signal, label="Continuous")
            ax.stem(t_discrete, discrete_signal, use_line_collection=True, label="Discrete")

        ax.set_title(f"{self.wave_type.get()} - {plot_type}")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        # ax.legend()

        # Clear any previous plots
        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
        canvas.draw()