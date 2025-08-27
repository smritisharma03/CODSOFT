import tkinter as tk
from tkinter import messagebox

# Function to update expression
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(key))

# Function to clear display
def clear():
    entry.delete(0, tk.END)

# Function to calculate result
def calculate():
    try:
        result = eval(entry.get().replace('×', '*').replace('÷', '/'))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid Expression")

# Create main window
root = tk.Tk()
root.title("Virtual Calculator")
root.geometry("330x450")
root.resizable(False, False)
root.configure(bg="#222831")

# Entry box for displaying input/output
entry = tk.Entry(root, font=("Arial", 20), bd=8, insertwidth=2, width=14, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('×', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

# Create buttons dynamically
for (text, row, col, colspan) in [(*btn, 1) if len(btn) == 3 else btn for btn in buttons]:
    action = calculate if text == '=' else clear if text == 'C' else lambda x=text: press(x)
    tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 16), bg="#393E46", fg="white",
              command=action).grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)

# Start the application
root.mainloop()