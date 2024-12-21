import tkinter
from task1 import Task1
from task2 import Task2
from task3 import Task3  # Import Task3
from taskFilters import TaskFilters


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

    # task5_frame = Task5(root)  # Add Task5
    # notebook.add(task5_frame, text="Task 5: DFT and IDFT")

    filters_frame = TaskFilters(root)  # Add Task5
    notebook.add(filters_frame, text="Task Practical: Filters")

    # task5_frame = Task5(root)  # Add Task5
    # notebook.add(task5_frame, text="Task 5: DFT and IDFT")

    root.mainloop()

