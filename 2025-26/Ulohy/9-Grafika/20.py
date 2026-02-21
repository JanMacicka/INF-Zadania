import math
import random
import tkinter as tk


WIDTH = 700
HEIGHT = 500

AMOUNT = 13
CENTER = 200, 200
RADIUS_SMALL = 25

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

radius_big = RADIUS_SMALL / math.sin(math.pi / AMOUNT)
points = []

for i in range(AMOUNT):
    angle = 2 * math.pi * i / AMOUNT
    x = CENTER[0] + radius_big * math.cos(angle)
    y = CENTER[1] + radius_big * math.sin(angle)

    points.append((x, y))

for (x, y) in points:
    color = "#" + format(random.randint(0, 256 ** 3 - 1), "06x")

    canvas.create_oval(x - RADIUS_SMALL, y - RADIUS_SMALL, x + RADIUS_SMALL, y + RADIUS_SMALL, fill=color)
    
root.mainloop()
