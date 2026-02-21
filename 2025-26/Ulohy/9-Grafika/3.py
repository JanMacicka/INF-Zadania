import tkinter as tk


WIDTH = 700
HEIGHT = 500
MARGIN = 5

X = 50
Y = 50
A1 = 180
A2 = 100

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")

canvas.pack()

rect_1 = (X, Y, X + A1, Y + A1)
rect_2 = (X + (A1 - A2) / 2, Y + (A1 - A2) / 2)

canvas.create_rectangle(rect_1[0], rect_1[1], rect_1[2], rect_1[3], fill="indian red")
canvas.create_rectangle(rect_2[0], rect_2[1], rect_2[0] + A2, rect_2[1] + A2, fill="light blue")

canvas.create_text(rect_1[0] - MARGIN, rect_1[1] - MARGIN, text="D")
canvas.create_text(rect_1[2] + MARGIN, rect_1[1] - MARGIN, text="C")
canvas.create_text(rect_1[0] - MARGIN, rect_1[3] + MARGIN, text="A")
canvas.create_text(rect_1[2] + MARGIN, rect_1[3] + MARGIN, text="B")

canvas.create_text(rect_1[2] + MARGIN * 2, rect_1[1] + A1 / 2, text=A1)
canvas.create_text(rect_2[0] + A2 / 2, rect_2[1] + A2 - 1.5 * MARGIN, text=A2)

root.mainloop()
