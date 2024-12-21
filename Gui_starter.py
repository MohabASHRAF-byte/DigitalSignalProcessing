import tkinter
from Gui.task1_gui import Task1
from Gui.task2_gui import Task2
from Gui.task3_gui import Task3  # Import Task3
from Gui.taskCorrelation_gui import TaskCorrelation
from Gui.taskFilters_gui import TaskFilters


# from task5 import Task5

def setup_gui():
    root = tkinter.Tk()
    root.geometry("870x600")
    root.minsize(width=800, height=800)
    style = tkinter.ttk.Style()
    style.configure('W.TButton', font=('Arial', 12, 'bold'))

    root.title("Signal Operations")

    notebook = tkinter.ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Add task tabs
    task1_frame = Task1(root)
    notebook.add(task1_frame, text="Task 1: Signal Operations")

    task2_frame = Task2(root)
    notebook.add(task2_frame, text="Task 2: Sine & Cosine")

    task3_frame = Task3(root)  # Add Task3
    notebook.add(task3_frame, text="Task 3: Signal Quantization")

    correlation_frame = TaskCorrelation(root)  # Add Task5
    notebook.add(correlation_frame, text="Task Practical: Correlation")

    filters_frame = TaskFilters(root)  # Add Task5
    notebook.add(filters_frame, text="Task Practical: Filters")

    root.mainloop()
