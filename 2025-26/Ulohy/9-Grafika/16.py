import tkinter as tk


WIDTH = 700
HEIGHT = 500

COLORS = ["maroon", "gold"]
SIZE = 30
SEPARATION = 3
MARGIN = 10

rows = int(input("zadajte pocet riadkov: "))
columns = int(input("zadajte pocet stlpcov: "))

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

for i in range(rows * columns):
    x1 = (i % columns) * (SIZE + SEPARATION) + MARGIN
    y1 = (i // columns) * (SIZE + SEPARATION) + MARGIN
    x2 = x1 + SIZE
    y2 = y1 + SIZE

    if (i // columns) % 2 == 0 or columns % 2 == 1:
        color = COLORS[i % 2]
    else:
        color = COLORS[1 - i % 2]

    canvas.create_rectangle(x1, y1, x2, y2, fill=color)
    
root.mainloop()
