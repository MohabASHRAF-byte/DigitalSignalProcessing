from tkinter import *
from tkinter import ttk, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from EquationParser import EquationParser
from Signal import Signal

root = Tk()
root.geometry("800x600")
root.minsize(width=800, height=800)

root.title("Signal Operations")

# Configure the grid layout of the root window
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

# Dictionaries to store the signals
dic = {}
dic1 = {}
variables = {}

ep = EquationParser(variables)
def open_file(dictionary):
    file_path = filedialog.askopenfilename(
        title="Select a Text File", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            dictionary.clear()
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    index = int(parts[0])
                    value = float(parts[1])
                    dictionary[index] = value
        plot_signals()

def open_file_1():
    global ep
    open_file(dic)
    variables["s1"] = Signal(data=dic, offset=5)
    if 's1' in variables.keys() and 's2' in variables.keys():
        ep = EquationParser(variables)

def open_file_2():
    global ep
    open_file(dic1)
    variables["s2"] = Signal(data=dic1, offset=5)
    if 's1' in variables.keys() and 's2' in variables.keys():
        ep = EquationParser(variables)

def plot_signals():
    fig, axs = plt.subplots(1, 2, figsize=(8, 3))

    if dic:
        axs[0].stem(dic.keys(), dic.values(), use_line_collection=True)
        axs[0].set_title("Signal 1")
    else:
        axs[0].text(0.5, 0.5, "No Data", ha='center', va='center')

    if dic1:
        axs[1].stem(dic1.keys(), dic1.values(), use_line_collection=True)
        axs[1].set_title("Signal 2")
    else:
        axs[1].text(0.5, 0.5, "No Data", ha='center', va='center')

    for widget in plot_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
    canvas.draw()

def add_signals():
    result = ep.evaluate("s1 + s2")
    plot_result(result, "Addition Result")

def subtract_signals():
    result = ep.evaluate("s1 - s2")
    plot_result(result, "Subtraction Result")

def multiply_signals():
    result = ep.evaluate("s1 * 5")
    plot_result(result, "Multiplication Result")

def advance_signals():
    s1 = Signal(data=dic)
    result = s1.DelayingOrAdvancingSignalByK(3)
    plot_result(result, "Advance S1 by 3 Result")

def delay_signals():
    s1 = Signal(data=dic)
    result = s1.DelayingOrAdvancingSignalByK(-3)
    plot_result(result, "Delay S1 by 3 Result")

def mirror_signals():
    s1 = Signal(data=dic)
    result = s1.mirror()
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

button_frame = ttk.Frame(root)
button_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=5)

equation_frame = ttk.Frame(root, borderwidth=2)
equation_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

equation_label = ttk.Label(equation_frame, text="Enter Equation (e.g., s1 + s2):")
equation_label.grid(row=0, column=0, padx=5, pady=5)

equation_entry = ttk.Entry(equation_frame, width=40)
equation_entry.grid(row=0, column=1, padx=5, pady=5)

def evaluate_equation():
    equation = equation_entry.get()
    result = ep.evaluate(equation)
    plot_result(result, f"Result of {equation}")

evaluate_button = ttk.Button(equation_frame, text="Evaluate", command=evaluate_equation)
evaluate_button.grid(row=0, column=2, padx=5, pady=5)

plot_frame = ttk.Frame(root, borderwidth=2, relief="solid")
plot_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)

result_frame = ttk.Frame(root, borderwidth=2, relief="solid")
result_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

def evaluate_equation(equation, plot_title):
    result = ep.evaluate(equation)
    plot_result(result, plot_title)

def add_button(row, column, text, command):
    button = ttk.Button(button_frame, text=text, command=command)
    button.grid(row=row, column=column, padx=5, pady=(15, 0))

add_button(0, 0, "Open File 1", open_file_1)
add_button(0, 1, "Open File 2", open_file_2)
add_button(0, 2, "Add Signals", lambda: evaluate_equation("s1 + s2", "Addition Result"))
add_button(0, 3, "Subtract Signals", lambda: evaluate_equation("s1 - s2", "Subtraction Result"))
add_button(0, 4, "Multiply S1 by 5", lambda: evaluate_equation("s1 * 5", "Multiply S1 by 5 Result"))
add_button(0, 5, "Delay S1 by 3", delay_signals)
add_button(0, 6, "Advance S1 by 3", advance_signals)

root.mainloop()
