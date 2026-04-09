import tkinter as tk


WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
NOTES_PER_LINE = 20
LINE_SEPARATION = 10
Y_MARGIN = 10
STAFF_SEPARATION = 100
HELP_LINE_WIDTH = 15
NOTE_COORDS = {"c": 5 * LINE_SEPARATION,
               "d": 4.5 * LINE_SEPARATION,
               "e": 4 * LINE_SEPARATION,
               "f": 3.5 * LINE_SEPARATION,
               "g": 3 * LINE_SEPARATION,
               "a": 2.5 * LINE_SEPARATION,
               "h": 2 * LINE_SEPARATION}

root = tk.Tk()
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

canvas.pack()


def draw_lines(start_y):
    for i in range(5):
        x1 = 0
        x2 = WINDOW_WIDTH
        y1 = start_y + i * LINE_SEPARATION
        y2 = y1

        canvas.create_line(x1, y1, x2, y2)


notes = []

with open("24-Noty.txt", "r") as f:
    notes = [n for n in f.readline().strip()]

staffs = len(notes) // NOTES_PER_LINE

if len(notes) % NOTES_PER_LINE > 0:
    staffs += 1

for i in range(staffs):
    draw_lines(Y_MARGIN + i * STAFF_SEPARATION)

for i, note in enumerate(notes):
    x = i % NOTES_PER_LINE * (WINDOW_WIDTH / NOTES_PER_LINE) + (WINDOW_WIDTH / NOTES_PER_LINE) / 2
    y = Y_MARGIN + (i // NOTES_PER_LINE * STAFF_SEPARATION) + NOTE_COORDS[note]

    canvas.create_oval(x - LINE_SEPARATION / 2, y - LINE_SEPARATION * (1 / 3), x + LINE_SEPARATION / 2, y + LINE_SEPARATION * (1 / 3))

    if note == "c":
        canvas.create_line(x - HELP_LINE_WIDTH / 2, y, x + HELP_LINE_WIDTH / 2, y)

root.mainloop()
