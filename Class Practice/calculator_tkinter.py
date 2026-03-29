import tkinter as tk
from tkinter import messagebox

def add():
    a = int(e1.get())
    b = int(e2.get())
    messagebox.showinfo("Result", a + b)

def sub():
    a = int(e1.get())
    b = int(e2.get())
    messagebox.showinfo("Result", a - b)

def mul():
    a = int(e1.get())
    b = int(e2.get())
    messagebox.showinfo("Result", a * b)

def div():
    a = int(e1.get())
    b = int(e2.get())
    messagebox.showinfo("Result", a / b)

tk.Label(text="Simple Calculator", bg="lightblue", font=("Arial", 16)).pack()

tk.Label(text="First Number", bg="lightyellow", font=("Arial", 12)).pack()
e1 = tk.Entry(font=("Arial", 12))
e1.pack()

tk.Label(text="Second Number", bg="lightyellow", font=("Arial", 12)).pack()
e2 = tk.Entry(font=("Arial", 12))
e2.pack()

tk.Button(text="+", font=("Arial", 12), bg="lightgreen", width=10, command=add).pack()
tk.Button(text="-", font=("Arial", 12), bg="lightgreen", width=10, command=sub).pack()
tk.Button(text="*", font=("Arial", 12), bg="lightgreen", width=10, command=mul).pack()
tk.Button(text="/", font=("Arial", 12), bg="lightgreen", width=10, command=div).pack()

tk.mainloop()