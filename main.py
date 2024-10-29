from tkinter import ttk, font, Tk
from task1 import Task1
from task2 import Task2
from task3 import Task3  # Import Task3

def setup_gui():
    root = Tk()
    root.geometry("870x600")
    root.minsize(width=800, height=800)
    custom_font = font.Font(family="Arial", size=12, weight="bold")
    style = ttk.Style()
    style.configure('W.TButton', font=('Arial', 12, 'bold'))

    root.title("Signal Operations")

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Add task tabs
    task1_frame = Task1(root)
    notebook.add(task1_frame, text="Task 1: Signal Operations")

    task2_frame = Task2(root)
    notebook.add(task2_frame, text="Task 2: Sine & Cosine")

    task3_frame = Task3(root)  # Add Task3
    notebook.add(task3_frame, text="Task 3: Signal Quantization")

    root.mainloop()

if __name__ == "__main__":
    setup_gui()
