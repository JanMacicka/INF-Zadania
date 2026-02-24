import random
import tkinter as tk

WIDTH = 700
HEIGHT = 500

MARGIN = 10
ROW_HEIGHT = 40
FONT = "Consolas 30"
CIRCLE_DIAMETER = 10
CIRCLE_SEPARATION = 4

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

dividend = random.randint(11, 20)
divisor = random.randint(2, 9)
result = dividend // divisor

dividend_colors = ["red", "green", "blue"]


def check_input() -> None:
    result_given = int(input_box.get())

    if result_given == result:
        text = "SPRÁVNE"
    else:
        text = "NESPRÁVNE"

    canvas.create_text(MARGIN, MARGIN + ROW_HEIGHT, text=text, anchor="nw", font=FONT)

    current_color_index = 0

    for i in range(divisor * (dividend // divisor)):
        x1 = MARGIN + i * (CIRCLE_DIAMETER + CIRCLE_SEPARATION)
        y1 = MARGIN + ROW_HEIGHT * 2 + 5
        x2 = x1 + CIRCLE_DIAMETER
        y2 = y1 + CIRCLE_DIAMETER

        canvas.create_oval(x1, y1, x2, y2, fill=dividend_colors[current_color_index % len(dividend_colors)], outline="")

        if (i + 1) % divisor == 0:
            current_color_index += 1

    for i in range(dividend % divisor):
        x1 = MARGIN + (divisor * (dividend // divisor) + i + 1) * (CIRCLE_DIAMETER + CIRCLE_SEPARATION)
        y1 = MARGIN + ROW_HEIGHT * 2 + 5
        x2 = x1 + CIRCLE_DIAMETER
        y2 = y1 + CIRCLE_DIAMETER
    
        canvas.create_oval(x1, y1, x2, y2, fill="yellow", outline="")


canvas.create_text(MARGIN, MARGIN, text=f"{dividend} : {divisor} = ", anchor="nw", font=FONT)

input_box = tk.Entry(root, width=5)
button = tk.Button(root, text="SKONTROLUJ", command=check_input)

input_box.place(x=MARGIN + 200, y=MARGIN + ROW_HEIGHT / 2 + 5, anchor="w")
button.place(x=MARGIN + 250, y=MARGIN + ROW_HEIGHT / 2 + 5, anchor="w")

root.mainloop()
