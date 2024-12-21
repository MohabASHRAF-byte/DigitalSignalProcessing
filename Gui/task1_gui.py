from tkinter import ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from Signal import Signal
from Bonus.EquationParser import EquationParser


class Task1(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.signals = []
        self.variables = {}
        self.ep = EquationParser(self.variables)
        self.plot_frame = None
        self.result_frame = None
        self.setup_gui()

    def setup_gui(self):
        button_frame = ttk.Frame(self)
        button_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=5)

        equation_frame = ttk.Frame(self, borderwidth=2)
        equation_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        self.plot_frame = ttk.Frame(self, borderwidth=2, relief="solid")
        self.plot_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)

        self.result_frame = ttk.Frame(self, borderwidth=2, relief="solid")
        self.result_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

        self.create_widgets(button_frame, equation_frame)

    def create_widgets(self, button_frame, equation_frame):
        equation_label = ttk.Label(
            equation_frame,
            text="Enter Equation (e.g., s1 + s2):"
        )
        equation_label.grid(row=0, column=0, padx=5, pady=5)

        self.equation_entry = ttk.Entry(equation_frame, width=40)
        self.equation_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create and add buttons
        self.add_button(button_frame, 0, 0, "Open File", self.open_file)
        self.add_button(
            button_frame, 0, 2, "S1 + S2",
            lambda: self.evaluate_equation("s1 + s2", "Addition Result")
        )
        self.add_button(button_frame, 0, 3, "Subtract Signals",
                        lambda: self.evaluate_equation("s1 - s2",
                                                       "Subtraction Result"))
        self.add_button(button_frame, 0, 4, "Multiply S1 by 5",
                        lambda: self.evaluate_equation("s1 * 5",
                                                       "Multiply S1 by 5 Result"
                                                       ))
        self.add_button(button_frame, 0, 5, "Delay S1 by 3", self.delay_signals)
        self.add_button(button_frame, 0, 6, "Advance S1 by 3", self.advance_signals)

    def add_button(self, frame, row, column, text, command):
        button = ttk.Button(frame, text=text, command=command)
        button.grid(row=row, column=column, padx=5, pady=7.5)

    def open_file(self):
        file_paths = filedialog.askopenfilenames(
            title="Select Text Files",
            filetypes=[("Text files", "*.txt")]
        )
        if file_paths:
            for file_path in file_paths:
                with open(file_path, 'r') as file:
                    data = {}
                    for line in file:
                        parts = line.strip().split()
                        if len(parts) == 2:
                            index = int(parts[0])
                            value = float(parts[1])
                            data[index] = value
                    self.signals.append(Signal(data))
            self.update_variables()
            self.plot_signals()

    def update_variables(self):
        self.variables.clear()
        for idx, signal in enumerate(self.signals):
            self.variables[f"s{idx + 1}"] = signal
        self.ep = EquationParser(self.variables)

    def plot_signals(self):
        fig, axs = plt.subplots(1, len(self.signals), figsize=(8, 3))
        if len(self.signals) == 1:
            axs = [axs]  # Make iterable if only one signal

        for ax, signal in zip(axs, self.signals):
            ax.stem(signal.data.keys(),
                    signal.data.values(),
                    use_line_collection=True
                    )
            ax.set_title(f"Signal {self.signals.index(signal) + 1}")

        for i in range(len(self.signals), len(axs)):
            axs[i].axis('off')  # Hide unused subplots

        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
        canvas.draw()

    def advance_signals(self):
        result = self.signals[0].DelayingOrAdvancingSignalByK(3)
        self.plot_result(result, "Advance S1 by 3 Result")

    def delay_signals(self):
        result = self.signals[0].DelayingOrAdvancingSignalByK(-3)
        self.plot_result(result, "Delay S1 by 3 Result")

    def mirror_signals(self):
        result = self.signals[0].mirror()
        self.plot_result(result, "Fold S1")

    def plot_result(self, result, title):
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.stem(result.data.keys(), result.data.values(), use_line_collection=True)
        ax.set_title(title)

        for widget in self.result_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.result_frame)
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
        canvas.draw()

        self.export_result(result, title)

    def export_result(self, result, title):
        file_path = filedialog.asksaveasfilename(
            title=f"Save {title}",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )
        if file_path:
            with open(file_path, 'w') as file:
                file.write("0\n")
                file.write("0\n")
                file.write("12\n")
                for index, value in result.data.items():
                    file.write(f"{index} {value}\n")

    def evaluate_equation(self, equation, plot_title):
        result = self.ep.evaluate(equation)
        self.plot_result(result, plot_title)
