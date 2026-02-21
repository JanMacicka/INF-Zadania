import tkinter as tk


WIDTH = 700
HEIGHT = 500

SIZE = 50
START = 180, 250

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

colors = ["dark green", "forest green", "yellow green", "lime green"]

for i in range(1, 5):
    x1 = START[0] + i * SIZE / 2
    y1 = START[1] - i * SIZE
    x2 = x1 + (5 - i) * SIZE
    y2 = y1 + SIZE
    canvas.create_rectangle(x1, y1, x2, y2, fill=colors[i - 1])

root.mainloop()
