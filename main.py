# main file
import tkinter as tk
from tkinter import messagebox
import function as calc

def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression, {"__builtins__": None}, calc.__dict__)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Input: {e}")

def append_to_expression(symbol):
    entry.insert(tk.END, str(symbol))

def clear_entry():
    entry.delete(0, tk.END)

def calculate_unary_operation(operation):
    try:
        value = float(entry.get())
        result = getattr(calc, operation)(value)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Operation: {e}") 

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("340x680")

entry = tk.Entry(root, font = ("Arial", 20), bd = 10, insertwidth = 2, width = 14, justify = "right")
entry.grid(row = 0, column = 0, columnspan = 4, sticky ="w")

button_texts = [
    (" 7 ", 1, 0), (" 8 ", 1, 1), (" 9 ", 1, 2), (" / ", 1, 3),
    (" 4 ", 2, 0), (" 5 ", 2, 1), (" 6 ", 2, 2), (" * ", 2, 3),
    (" 1 ", 3, 0), (" 2 ", 3, 1), (" 3 ", 3, 2), (" - ", 3, 3),
    ("C", 4, 0), (" 0 ", 4, 1), ("  . ", 4, 2), (" + ", 4, 3),
]

for (text, row, col) in button_texts:
    tk.Button(root, text = text, padx = 20, pady = 20, font = ("Arial", 14), bg = "purple", fg = "white", command = lambda t = text: append_to_expression(t)).grid(row = row, column = col, sticky = "w")

unary_operations = {
    "1/x": "reciprocal", 
    "x^2": "square", 
    " √x ": "square_root", 
    "log": "logarithm",
    " ln ": "natural_log", 
    " sin": "sine", 
    "cos": "cosine", 
    "tan": "tangent"
}

row = 5
col = 0
for text, operation in unary_operations.items():
    tk.Button(root, text = text, padx = 20, pady = 20, font = ("Arial", 14), bg = "violet", fg = "white", command = lambda op = operation: calculate_unary_operation(op)).grid(row = row, column = col, sticky = "w")
    col += 1
    if col > 3:
        row += 1
        col = 0

tk.Button(root, text="=", padx=20, pady=20, font=("Arial", 14), bg="lightblue", fg ="white", command=evaluate_expression).grid(row=row, column=0, columnspan=4, sticky="nsew")

tk.Button(root, text="Clear", padx=20, pady=20, font=("Arial", 14), bg="lightcoral", fg = "white", command=clear_entry).grid(row=row+1, column=0, columnspan=4, sticky="nsew")

root.mainloop()
