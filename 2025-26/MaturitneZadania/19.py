import tkinter as tk


class Stop:
    def __init__(self, name: str, express: bool) -> None:
        self.name = name
        self.express = express


    def __str__(self) -> str:
        return self.name


WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
STOP_SEPARATION = 25
LINE_WIDTH = 1.5
X_MARGIN = 10
Y_MARGIN = 100
STOP_RADIUS = 3

root = tk.Tk()
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

canvas.pack()

color = ""
stops = []

with open("19-TrasaLinkyMetra.txt", "r") as f:
    color = f.readline().strip()

    for row in f.readlines():
        row = row.strip()
        express = row.startswith("*")
        name = row if not express else row[1:]

        stops.append(Stop(name, express))

x1 = X_MARGIN
y1 = Y_MARGIN
x2 = x1 + (len(stops) - 1) * STOP_SEPARATION
y2 = y1

canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)

for i, stop in enumerate(stops):
    x1 = X_MARGIN + i * STOP_SEPARATION - STOP_RADIUS
    y1 = Y_MARGIN - STOP_RADIUS
    x2 = x1 + 2 * STOP_RADIUS
    y2 = y1 + 2 * STOP_RADIUS

    canvas.create_text(x1 + 8, y1 - STOP_RADIUS, anchor="sw", angle=45, text=stop.name, font="Arial 8")

    if i == 0 or i == len(stops) - 1:
        canvas.create_rectangle(x1 - 2, y1 - 2, x2 + 2, y2 + 2, fill=color, outline="")
        continue

    fill = color if not stop.express else "white"

    canvas.create_oval(x1, y1, x2, y2, outline=color, fill=fill, width=LINE_WIDTH / 2)

root.mainloop()
