import random
import tkinter as tk


WIDTH = 700
HEIGHT = 500

AMOUNT = 20

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

for i in range(AMOUNT):
    size = random.randint(10, 50)
    x1 = random.randint(0 - size, WIDTH + size)
    y1 = random.randint(0 - size, HEIGHT + size)
    x2 = x1 + size
    y2 = y1 + size
    a = (x1, y1)
    b = (x1 + size, y1)
    c = (x1 + size / 2, y1 - size * 3 ** (1/2) / 2)
    house_color = "#" + format(random.randint(0, 256 ** 3 - 1), "06x")
    roof_color = "#" + format(random.randint(0, 256 ** 3 - 1), "06x")

    canvas.create_rectangle(x1, y1, x2, y2, fill=house_color, outline="")
    canvas.create_polygon(a[0], a[1], b[0], b[1], c[0], c[1], fill=roof_color, outline="")
    
root.mainloop()
