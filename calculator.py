import tkinter as tk
import math



def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + button_text)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

history = []

def calculate():
    try:
        expr = entry.get()
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        history.append(f"{expr} = {result}")
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Cannot divide by 0")
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def sqrt_num():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(math.sqrt(value)))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")



root = tk.Tk()
root.title("Smart Calculator")
root.geometry("320x520")
root.config(bg="white")

entry = tk.Entry(root, width=18, font=("Arial", 22), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)



buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]

buttons_list = []

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, command=calculate, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"))
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: click(t), font=("Arial", 14, "bold"))
    btn.grid(row=row, column=col, padx=5, pady=5)
    buttons_list.append(btn)


clear_button = tk.Button(root, text="C", width=5, height=2, command=clear, bg="#F44336", fg="white", font=("Arial", 14, "bold"))
clear_button.grid(row=5, column=0, padx=5, pady=5)

back_button = tk.Button(root, text="←", width=5, height=2, command=backspace, bg="#9C27B0", fg="white", font=("Arial", 14, "bold"))
back_button.grid(row=5, column=1, padx=5, pady=5)

sqrt_button = tk.Button(root, text="√", width=5, height=2, command=sqrt_num, bg="#2196F3", fg="white", font=("Arial", 14, "bold"))
sqrt_button.grid(row=5, column=2, padx=5, pady=5)

history_button = tk.Button(root, text="📜", width=5, height=2, command=lambda: show_history(), bg="#FF9800", fg="white", font=("Arial", 14, "bold"))
history_button.grid(row=5, column=3, padx=5, pady=5)

buttons_list.extend([clear_button, back_button, sqrt_button, history_button])


def show_history():
    if not history:
        tk.messagebox.showinfo("History", "No calculations yet.")
        return
    hist_window = tk.Toplevel(root)
    hist_window.title("History")
    hist_window.geometry("250x300")
    hist_window.config(bg="white")
    tk.Label(hist_window, text="History", font=("Arial", 14, "bold"), bg="white").pack(pady=5)
    text_box = tk.Text(hist_window, font=("Arial", 12), bg="#f8f8f8", height=15, width=25)
    text_box.pack(padx=10, pady=10)
    for item in history[-15:][::-1]:
        text_box.insert(tk.END, item + "\n")
    text_box.config(state="disabled")



dark_mode = False

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.config(bg="#222")
        entry.config(bg="#333", fg="white", insertbackground="white")
        for btn in buttons_list:
            btn.config(bg="#444", fg="white", activebackground="#555")
        theme_button.config(text="☀️ Light Mode", bg="#444", fg="white")
    else:
        root.config(bg="white")
        entry.config(bg="white", fg="black", insertbackground="black")
        for btn in buttons_list:
            btn.config(bg="#f0f0f0", fg="black", activebackground="#ddd")
        theme_button.config(text="🌙 Dark Mode", bg="#f0f0f0", fg="black")

theme_button = tk.Button(root, text="🌙 Dark Mode", width=20, height=2, command=toggle_theme, font=("Arial", 12, "bold"))
theme_button.grid(row=6, column=0, columnspan=4, pady=10)


root.mainloop()

