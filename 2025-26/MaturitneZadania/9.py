import random
import tkinter as tk


WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300

LINE_WIDTH = 10
LINE_HEIGHT = 80
LINES = 8
TEXT_HEIGHT = 15
ROWS = 2
COLUMNS = 2
CODES_PER_PAGE = ROWS * COLUMNS
X_MARGIN = 10
Y_MARGIN = 10
CODE_WIDTH = LINES * LINE_WIDTH

page_index = 0
codes = []

root = tk.Tk()
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

canvas.pack()


def generate_code(code: str, start_x: int, start_y: int) -> None:
    values = [int(x) for x in code]

    for i, value in enumerate(values):
        x1 = start_x + i * LINE_WIDTH
        y1 = start_y
        x2 = x1 + value
        y2 = start_y + LINE_HEIGHT

        if i == 0 or i == len(values) - 1:
            y2 += TEXT_HEIGHT

        canvas.create_rectangle(x1, y1, x2, y2, fill="black")

    x = start_x + LINES * LINE_WIDTH / 2
    y = start_y + LINE_HEIGHT + TEXT_HEIGHT / 2

    canvas.create_text(x, y, text=code)


def display_page() -> None:
    canvas.delete("all")

    start = page_index * CODES_PER_PAGE
    end = start + CODES_PER_PAGE
    page_codes = codes[start:end]
    
    for i, code in enumerate(page_codes):
        x = X_MARGIN + i % COLUMNS * (CODE_WIDTH + X_MARGIN)
        y = Y_MARGIN + i // COLUMNS * (LINE_HEIGHT + TEXT_HEIGHT + Y_MARGIN)

        generate_code(code, x, y)


def next_page(event=None) -> None:
    global page_index

    max_page = (len(codes) - 1) // CODES_PER_PAGE

    if page_index < max_page:
        page_index += 1
    else:
        page_index = 0

    display_page()


codes.append(str(random.randint(10000000, 99999999)))

with open("9-CiarovyKod-1.txt", "r") as f:
    for row in f.readlines():
        codes.append(row.strip())

display_page()

root.bind("<space>", next_page)
root.mainloop()
