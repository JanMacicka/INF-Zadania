import tkinter as tk


N = 25

WIDTH = N * 15
HEIGHT = 250

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

for i in range(N):
    b = round(i * 256 / N)
    r = 255 - b

    canvas.create_rectangle(i * 15, 0, (i + 1) * 15, HEIGHT, fill=f"#{r:02x}00{b:02x}", outline="")

root.mainloop()
