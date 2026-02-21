import tkinter as tk


WIDTH = 700
HEIGHT = 500

X = 50
Y = 50

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")

canvas.pack()

canvas.create_rectangle(X, Y, X + 100, Y + 100, fill="red")
canvas.create_rectangle(X + 100 + 10, Y, X + 200 + 10, Y + 100, fill="blue")
canvas.create_text(X + 50, Y + 50, text="červený", font="arial 20", fill="yellow")
canvas.create_text(X + 100 + 10 + 50, Y + 50, text="modrý", font="arial 20", fill="yellow")

root.mainloop()
