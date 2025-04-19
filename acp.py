from tkinter import *
from datetime import date

root = Tk()
root.title('Basic Arithmetic Calculator')
root.geometry('400x350')
root.configure(bg="#1A1A40")

lbl = Label(text="✨ Let's Do Some Math! ✨", fg="white", bg="#3F0071", height=2, font=("Arial", 14, "bold"))
lbl.pack(fill=X)

n1_lbl = Label(text="🔢 Enter Number 1", bg="#150050", fg="white", font=("Arial", 11))
n1_lbl.pack(pady=(10, 0))
n1_entry = Entry(font=("Arial", 12), bg="#E0E0E0", fg="#1A1A1A")
n1_entry.pack(pady=(0, 10))

n2_lbl = Label(text="🔢 Enter Number 2", bg="#150050", fg="white", font=("Arial", 11))
n2_lbl.pack()
n2_entry = Entry(font=("Arial", 12), bg="#E0E0E0", fg="#1A1A1A")
n2_entry.pack(pady=(0, 10))

text_box = Text(height=3, font=("Consolas", 12), bg="#F3F3F3", fg="#000", bd=0)
text_box.pack(pady=10)

def calculate(op):
    try:
        n1 = float(n1_entry.get())
        n2 = float(n2_entry.get())
        if op == 'add':
            result = n1 + n2
            operation = '+'
        elif op == 'subtract':
            result = n1 - n2
            operation = '-'
        elif op == 'multiply':
            result = n1 * n2
            operation = '*'
        elif op == 'divide':
            result = n1 / n2 if n2 != 0 else 'Infinity'
            operation = '/'
        text_box.insert(END, f"{n1} {operation} {n2} = {result}\n")
    except ValueError:
        text_box.insert(END, "🚫 Please enter valid numbers.\n")

btn_style = {"bg": "#4E31AA", "fg": "white", "font": ("Arial", 11, "bold"), "width": 15, "pady": 5}
Button(text="➕ Add", command=lambda: calculate('add'), **btn_style).pack(pady=2)
Button(text="➖ Subtract", command=lambda: calculate('subtract'), **btn_style).pack(pady=2)
Button(text="✖ Multiply", command=lambda: calculate('multiply'), **btn_style).pack(pady=2)
Button(text="➗ Divide", command=lambda: calculate('divide'), **btn_style).pack(pady=2)

root.mainloop()
