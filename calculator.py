import tkinter as tk

def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, width=16, font=("Arial", 20), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, command=calculate, bg="#4CAF50", fg="white")
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

clear_button = tk.Button(root, text="C", width=22, height=2, command=clear, bg="#F44336", fg="white")
clear_button.grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()

