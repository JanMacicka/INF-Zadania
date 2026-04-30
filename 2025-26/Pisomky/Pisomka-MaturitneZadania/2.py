import os
import random
import time
import tkinter as tk


WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
MARGIN = 50
PLATE_SEPARATION = 50
PLATE_RADIUS = 20

root = tk.Tk()
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

canvas.pack()

ticket_position = random.randint(0, 8)

x1 = MARGIN + ticket_position * PLATE_SEPARATION - PLATE_RADIUS
y1 = MARGIN
x2 = x1 + 2 * PLATE_RADIUS
y2 = y1 + 2 * PLATE_RADIUS

canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="")

for i in range(9):
    x1 = MARGIN + i * PLATE_SEPARATION - PLATE_RADIUS
    y1 = MARGIN
    x2 = x1 + 2 * PLATE_RADIUS
    y2 = y1 + 2 * PLATE_RADIUS
    canvas.create_oval(x1, y1, x2, y2, fill="blue")
    canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10)
    canvas.create_text(x1 + PLATE_RADIUS - 2.5, y1 + PLATE_RADIUS * 2 + 10, anchor="nw", text=f"{i + 1}.")

guessed = False

while not guessed:
    os.system("cls")
    
    guess = int(input("zadajte cislo taniera: "))

    if guess > ticket_position + 1:
        print("vlavo")
    elif guess < ticket_position + 1:
        print("vpravo")
    else:
        print("spravne!")
        break

    time.sleep(1)

root.mainloop()
