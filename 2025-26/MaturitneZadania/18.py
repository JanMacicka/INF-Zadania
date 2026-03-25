import tkinter as tk


class Information:
    def __init__(self, position: tuple[int], name: str, snow_level: int, conditions: str) -> None:
        self.position = position
        self.name = name
        self.snow_level = snow_level
        self.conditions = conditions


    def __str__(self) -> str:
        return f"{self.name}: {self.snow_level} cm, podmienky {self.conditions}"


WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
DOT_RADIUS = 0.1
INFORMATION_RADIUS = 5
Y_DELTA = -115

page_index = 0
borders = []
information = []

root = tk.Tk()
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

canvas.pack()


def display_page() -> None:
    canvas.delete("all")

    for point in borders:
        canvas.create_oval(point[0] - DOT_RADIUS, point[1] - DOT_RADIUS, point[0] + DOT_RADIUS, point[1] + DOT_RADIUS, fill="green", outline="")

    current_information = information[page_index]
    position = current_information.position

    canvas.create_oval(position[0] - INFORMATION_RADIUS, position[1] - INFORMATION_RADIUS + Y_DELTA, position[0] + INFORMATION_RADIUS, position[1] + INFORMATION_RADIUS + Y_DELTA, fill="black")
    canvas.create_text(20, 350, anchor="nw", text=current_information, font="Arial 20")


def next_page(event=None) -> None:
    global page_index

    page_index += 1

    if page_index >= len(information):
        page_index = 0

    display_page()


with open("18-SR.txt", "r") as f:
    for row in f.readlines():
        borders.append(tuple([int(x) for x in row.split()]))

with open("18-Sneh.txt") as f:
    for row in f.readlines():
        values = row.split(" - ")
        position_name = values[0].split()
        name = " ".join(position_name[2:])

        information.append(Information((int(position_name[0]), int(position_name[1])), name, int(values[1][:-3]), values[2]))

display_page()

root.bind("<Key>", next_page)
root.mainloop()
