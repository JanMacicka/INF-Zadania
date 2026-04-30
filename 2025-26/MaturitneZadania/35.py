import random
import tkinter as tk


WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
MARGIN_BOTTOM = 100
TABLE_WIDTH = 100
TABLE_HEIGHT = 50
TABLE_SEPARATION = 15
MARGIN = 15

root = tk.Tk()
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

canvas.pack()

people = []

with open("35-ZasadaciPoriadok.csv", "r", encoding="ansi") as f:
    rows = f.readlines()

    for row in rows:
        people.append(row.strip().split(";"))


def check_input() -> None:
    canvas.delete("all")
    random.shuffle(people)

    rows = int(input_rows.get())
    tables_per_row = int(input_tables_per_row.get())

    if rows * tables_per_row < len(people):
        canvas.create_text(WINDOW_WIDTH / 2, (WINDOW_HEIGHT - MARGIN_BOTTOM) / 2, text="Mate malo lavic na usadenie studentov!", font="arial 20", fill="red")
        return
    
    for i in range(rows):
        for j in range(tables_per_row):
            x1 = j * (TABLE_WIDTH + TABLE_SEPARATION) + MARGIN
            x2 = x1 + TABLE_WIDTH
            y1 = i * (TABLE_HEIGHT + TABLE_SEPARATION) + MARGIN
            y2 = y1 + TABLE_HEIGHT

            canvas.create_rectangle(x1, y1, x2, y2)

            iterator = tables_per_row * i + j

            if iterator < len(people):
                canvas.create_text((x1 + x2) / 2, y1 + (y2 - y1) / 3, text=people[iterator][0], fill="red")
                canvas.create_text((x1 + x2) / 2, y1 + (y2 - y1) / 3 * 2, text=people[iterator][1], fill="blue")


label_rows = tk.Label(root, text="Pocet radov:")
input_rows = tk.Entry(root, width=5)
label_tables_per_row = tk.Label(root, text="Lavic v rade:")
input_tables_per_row = tk.Entry(root, width=5)
button = tk.Button(root, text="Potvrd vstup", command=check_input)

x = WINDOW_WIDTH / 2
y = WINDOW_HEIGHT - MARGIN_BOTTOM

label_rows.place(x=x, y=y, anchor="center")
input_rows.place(x=x, y=y + 15, anchor="center")
label_tables_per_row.place(x=x, y=y + 30, anchor="center")
input_tables_per_row.place(x=x, y=y + 45, anchor="center")
button.place(x=x, y=y + 80, anchor="center")

root.mainloop()
