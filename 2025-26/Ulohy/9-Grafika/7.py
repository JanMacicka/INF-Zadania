import tkinter as tk


WIDTH = 700
HEIGHT = 500

START_POS = 10, 100
DIFF = 20
AMOUNT = 16

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

for i in range(AMOUNT):
    x1 = START_POS[0] + i * DIFF
    y1 = START_POS[1] + (i % 2) * DIFF
    x2 = x1 + DIFF
    
    if y1 > START_POS[1]:
        y2 = START_POS[1]
    else:
        y2 = START_POS[1] + DIFF

    canvas.create_line(x1, y1, x2, y2, fill="blue", width=5)

root.mainloop()
