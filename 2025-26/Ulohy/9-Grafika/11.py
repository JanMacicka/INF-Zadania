import random
import tkinter as tk


WIDTH = 700
HEIGHT = 500

FONT = "arial 26"
SIZE = 30
OFFSET = 10, 100

text = input("zadajte text na vypisanie: ")

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

for i, char in enumerate(text):
    x1 = i * SIZE + OFFSET[0]
    y1 = OFFSET[1]
    x2 = x1 + SIZE
    y2 = y1 + SIZE
    
    color_bg = "#" + format(random.randint(0, 256 ** 3 - 1), "06x")
    color_text = "#" + format(random.randint(0, 256 ** 3 - 1), "06x")

    canvas.create_rectangle(x1, y1, x2, y2, fill=color_bg,)
    canvas.create_text(x1 + SIZE / 2, y1 + SIZE / 2, text=char, font=FONT, fill=color_text)
    
root.mainloop()
