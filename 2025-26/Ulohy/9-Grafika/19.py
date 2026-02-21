import math
import tkinter as tk


WIDTH = 700
HEIGHT = 500

CENTER = 180, 130
SIDES = 7
SIZE = 100

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

radius = SIZE / (2 * math.sin(math.pi / SIDES))
points = []

for i in range(SIDES):
    angle = 2 * math.pi * i / SIDES - math.pi / 2
    x = CENTER[0] + radius * math.cos(angle)
    y = CENTER[1] + radius * math.sin(angle)

    points.append((x, y))

for i in range(len(points) - 1):
    for j in range(i, len(points)):
        canvas.create_line(points[i][0], points[i][1], points[j][0], points[j][1], width=3)
    
root.mainloop()
