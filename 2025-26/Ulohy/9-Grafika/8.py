import tkinter as tk


WIDTH = 700
HEIGHT = 500

START = 70, 100
RADIUS = 50
ROW_SEPARATION = 60
COL_SEPARATION = 120
CIRCLE_WIDTH = 15

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

colors = ["blue", "yellow", "black", "lime green", "red"]

for i in range(5):
    if i % 2 == 0:
        x = START[0] + i / 2 * COL_SEPARATION
        y = START[1]

    else:
        x = START[0] + COL_SEPARATION / 2 + (i - 1) * COL_SEPARATION / 2
        y =  START[1] + ROW_SEPARATION

    canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS, fill="", outline=colors[i], width=CIRCLE_WIDTH)

root.mainloop()
