import tkinter as tk


WIDTH = 700
HEIGHT = 500

X, Y = 50, 250
SIZE = 280
COLOR = "blue"

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

a = (X, Y)
b = (X + SIZE, Y)
c = (X + SIZE / 2, Y - SIZE * 3 ** (1/2) / 2)

canvas.create_polygon(a[0], a[1], b[0], b[1], c[0], c[1], fill=COLOR)
    
root.mainloop()
