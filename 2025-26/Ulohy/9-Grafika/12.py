import random
import tkinter as tk


WIDTH = 400
HEIGHT = 300

SEPARATION = 5
START_X = 10
END_X = 380
AMOUNT = 7
Y_OFFSET = 75

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

square_size = (END_X - START_X - (AMOUNT - 1) * SEPARATION) / AMOUNT

for i in range(AMOUNT):
    x1 = START_X + i * (square_size + SEPARATION)
    y1 = Y_OFFSET
    x2 = x1 + square_size
    y2 = y1 + square_size
    color = "#" + format(random.randint(0, 256 ** 3 - 1), "06x")

    canvas.create_rectangle(x1, y1, x2, y2, fill=color)
    
root.mainloop()
