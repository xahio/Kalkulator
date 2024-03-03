import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Błąd")

def clear_entry():
    entry.delete(0, tk.END)

def add_to_entry(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(symbol))

root = tk.Tk()
root.title("Kalkulator")

entry = ttk.Entry(root, font=('Arial', 16), justify='right')
entry.grid(row=0, column=0, columnspan=5, sticky="nsew")

for i in range(9):
    ttk.Button(root, text=str(i + 1), command=lambda i=i: add_to_entry(i + 1)).grid(row=i // 3 + 1, column=i % 3, sticky="nsew")

math_operations = ['+', '-', '*', '/']
for i, operation in enumerate(math_operations):
    ttk.Button(root, text=operation, command=lambda operation=operation: add_to_entry(operation)).grid(row=i + 1, column=3, sticky="nsew")

ttk.Button(root, text='0', command=lambda: add_to_entry(0)).grid(row=4, column=0, columnspan=2, sticky="nsew")
ttk.Button(root, text='.', command=lambda: add_to_entry('.')).grid(row=4, column=2, sticky="nsew")
ttk.Button(root, text='=', command=calculate).grid(row=5, column=3, columnspan=2, sticky="nsew")

ttk.Button(root, text='C', command=clear_entry).grid(row=5, column=0, columnspan=3, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
