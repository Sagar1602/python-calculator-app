import tkinter as tk
from tkinter import messagebox

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def add_to_expression(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

# UI setup
root = tk.Tk()
root.title("Python Calculator")

entry = tk.Entry(root, width=20, font=('Arial', 24), bd=4, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
]

for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        if char == '=':
            btn = tk.Button(root, text=char, width=5, height=2, font=('Arial', 18), command=evaluate)
        else:
            btn = tk.Button(root, text=char, width=5, height=2, font=('Arial', 18), command=lambda ch=char: add_to_expression(ch))
        btn.grid(row=r+1, column=c, padx=5, pady=5)

clear_btn = tk.Button(root, text='C', width=22, height=2, font=('Arial', 18), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
