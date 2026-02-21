import random
import tkinter as tk


WIDTH = 700
HEIGHT = 500

RADIUS = 20
FONT = "arial 30"
AMOUNT = 30

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

for i in range(AMOUNT):
    x = random.randint(0 - RADIUS, WIDTH + RADIUS)
    y = random.randint(0 - RADIUS, HEIGHT + RADIUS)
    
    value = random.randint(1, 9)
    color = "#" + format(random.randint(0, 256 ** 3 - 1), "06x")
    
    canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS, fill=color, outline="black")
    canvas.create_text(x, y, text=value, font=FONT)

root.mainloop()
