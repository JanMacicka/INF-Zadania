import tkinter as tk


WIDTH = 700
HEIGHT = 500
X_OFFSET = 100
Y_OFFSET = 50
MARGIN = 5

N = 20

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")

canvas.pack()

colors = ["red", "blue", "yellow"]

for i in range(N):
    x1 = MARGIN * i + X_OFFSET
    y1 = MARGIN * i + Y_OFFSET
    x2y2 = 2 * MARGIN * N - i * MARGIN
    canvas.create_rectangle(x1, y1, x2y2 + X_OFFSET, x2y2 + Y_OFFSET, fill=colors[i % 3])

root.mainloop()
