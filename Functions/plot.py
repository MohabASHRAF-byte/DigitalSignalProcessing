"""
This class provides the functionality to plot a signal using matplotlib
within a Tkinter window.
"""

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Signal import Signal


class Plot:
    @staticmethod
    def plot(signal: Signal, title="Signal Plot"):
        """
        Plots the signal in a Tkinter window.
        """
        plot_window = tk.Toplevel()
        plot_window.title(title)

        indices = list(signal.data.keys())
        values = list(signal.data.values())

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(indices, values, marker="o", linestyle="-", color="b")
        ax.set_title(title)
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=plot_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        close_button = tk.Button(plot_window,
                                 text="Close",
                                 command=plot_window.destroy)
        close_button.pack(pady=10)
