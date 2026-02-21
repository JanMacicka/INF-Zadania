import random
import tkinter as tk


WIDTH = 700
HEIGHT = 500

OFFSET = 100, 20
AMOUNT = 10
RECT_MARGIN = 2
RECT_WIDTH = 50
RECT_HEIGHT = 20

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

num_sum = 0

for i in range(AMOUNT):
    value = random.choice((1, 2, 5, 10, 20, 50))
    num_sum += value

    x1 = OFFSET[0]
    y1 = OFFSET[1] + i * (RECT_HEIGHT + RECT_MARGIN)
    x2 = x1 + RECT_WIDTH
    y2 = y1 + RECT_HEIGHT
    
    canvas.create_rectangle(x1, y1, x2, y2)
    canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=f"{value} €", font="arial 15")

canvas.create_text(250, 50, text=f"spolu: {num_sum} €", font="arial 15")

root.mainloop()
