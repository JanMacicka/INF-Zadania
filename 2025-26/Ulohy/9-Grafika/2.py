import random
import tkinter as tk


WIDTH = 700
HEIGHT = 500

AMOUNT = 200

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="navy")

canvas.pack()

for i in range(AMOUNT):
    canvas.create_text(random.randint(0, WIDTH), random.randint(0, HEIGHT), text="*", font=f"arial {random.randint(10, 20)}", fill="yellow")

root.mainloop()
