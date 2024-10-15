from tkinter import ttk, filedialog, font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from EquationParser import EquationParser
from Signal import Signal

from ttkthemes import ThemedTk

root = ThemedTk(theme="breeze")
root.geometry("870x600")
root.minsize(width=800, height=800)
custom_font = font.Font(family="Arial", size=12, weight="bold")
style = ttk.Style()
style.configure('W.TButton', font = ('Arial', 12, 'bold'))

root.title("Signal Operations")

# Configure the grid layout of the root window
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

# List to store signals
signals = []
variables = {}
ep = EquationParser(variables)

def open_file():
    file_paths = filedialog.askopenfilenames(
        title="Select Text Files", filetypes=[("Text files", "*.txt")])
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
                signals.append(Signal(data))
        update_variables()
        plot_signals()

def update_variables():
    global ep
    variables.clear()
    for idx, signal in enumerate(signals):
        variables[f"s{idx + 1}"] = signal
    ep = EquationParser(variables)

def plot_signals():
    fig, axs = plt.subplots(1, len(signals), figsize=(8, 3))
    if len(signals) == 1:
        axs = [axs]  # Make it iterable if there's only one signal

    for ax, signal in zip(axs, signals):
        ax.stem(signal.data.keys(), signal.data.values(), use_line_collection=True)
        ax.set_title(f"Signal {signals.index(signal) + 1}")

    for i in range(len(signals), len(axs)):
        axs[i].axis('off')  # Hide unused subplots

    for widget in plot_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
    canvas.draw()

def advance_signals():
    result = signals[0].DelayingOrAdvancingSignalByK(3)
    plot_result(result, "Advance S1 by 3 Result")

def delay_signals():
    result = signals[0].DelayingOrAdvancingSignalByK(-3)
    plot_result(result, "Delay S1 by 3 Result")

def mirror_signals():
    result = signals[0].mirror()
    plot_result(result, "Fold S1")


def plot_result(result, title):
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.stem(result.data.keys(), result.data.values(), use_line_collection=True)
    ax.set_title(title)

    for widget in result_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=result_frame)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
    canvas.draw()

    export_result(result, title)

def export_result(result, title):
    file_path = filedialog.asksaveasfilename(
        title=f"Save {title}", defaultextension=".txt",
        filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write("0\n")
            file.write("0\n")
            file.write("12\n")
            for index, value in result.data.items():
                file.write(f"{index} {value}\n")

button_frame = ttk.Frame(root)
button_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=5)

equation_frame = ttk.Frame(root, borderwidth=2)
equation_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

equation_label = ttk.Label(equation_frame, text="Enter Equation (e.g., s1 + s2):", font=custom_font)
equation_label.grid(row=0, column=0, padx=5, pady=5)

equation_entry = ttk.Entry(equation_frame, width=40, font=custom_font)
equation_entry.grid(row=0, column=1, padx=5, pady=5)

def evaluate_equation():
    equation = equation_entry.get()
    result = ep.evaluate(equation)
    plot_result(result, f"Result of {equation}")

def add_button(frame, row, column, text, command):
    button = ttk.Button(frame, text=text, command=command, style="W.TButton")
    button.grid(row=row, column=column, padx=5, pady=(7.5, 7.5))

add_button(equation_frame, 0, 2, "Evaluate", evaluate_equation)

plot_frame = ttk.Frame(root, borderwidth=2, relief="solid")
plot_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)

result_frame = ttk.Frame(root, borderwidth=2, relief="solid")
result_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

def evaluate_equation(equation, plot_title):
    result = ep.evaluate(equation)
    plot_result(result, plot_title)

add_button(button_frame, 0, 0, "Open File", open_file)
add_button(button_frame, 0, 2, "S1 + S2", lambda: evaluate_equation("s1 + s2", "Addition Result"))
add_button(button_frame, 0, 3, "Subtract Signals", lambda: evaluate_equation("s1 - s2", "Subtraction Result"))
add_button(button_frame, 0, 4, "Multiply S1 by 5", lambda: evaluate_equation("s1 * 5", "Multiply S1 by 5 Result"))
add_button(button_frame, 0, 5, "Delay S1 by 3", delay_signals)
add_button(button_frame, 0, 6, "Advance S1 by 3", advance_signals)

root.mainloop()
