import tkinter as tk


WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
SQUARE_SIZE = 20
MARGIN = 10

root = tk.Tk()
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

canvas.pack()


def generate_crossword(words: list[tuple], area: tuple[int, int], hidden=True) -> None:
    center = (area[0] + area[1]) / 2

    for i, (position, word) in enumerate(words):
        for j, char in enumerate(word):
            x1 = center + (j + 1 - position) * SQUARE_SIZE - SQUARE_SIZE / 2
            x2 = x1 + SQUARE_SIZE
            y1 = i * SQUARE_SIZE + MARGIN
            y2 = y1 + SQUARE_SIZE
            fill = "grey" if j + 1 == position else ""

            canvas.create_rectangle(x1, y1, x2, y2, fill=fill)

            if not hidden:
                canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=char, font="Consolas 15")


words = []

with open("36-Krizovka1-1.txt", "r") as f:
    for row in f.readlines():
        values = row.split()
        words.append((int(values[0]), values[1]))

    generate_crossword(words, (0, WINDOW_WIDTH / 2))
    generate_crossword(words, (WINDOW_WIDTH / 2, WINDOW_WIDTH), hidden = False)

root.mainloop()
