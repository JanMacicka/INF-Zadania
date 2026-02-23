import tkinter as tk


WIDTH = 700
HEIGHT = 500
MARGIN = 20, 10
ROW_SEPARATOR = 30
RECT_START_SEPARATION_X = 90
PERC_MULTIPLIER = 3

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

question = ""
answer_labels = ["Áno", "Nie", "Neviem"]
answers = []


def display_page(question: str, answers: list[int]) -> None:
    canvas.delete("all")
    canvas.create_text(MARGIN[0], MARGIN[1], anchor="w", text=question)
    
    for i, answer in enumerate(answers):
        x = MARGIN[0]
        y = MARGIN[1] + (i + 1) * ROW_SEPARATOR

        canvas.create_text(x, y, anchor="w", text=f"{i + 1}) {answer_labels[i]} - {answer}")

        rect_x1 = MARGIN[0] + RECT_START_SEPARATION_X
        rect_y1 = y - ROW_SEPARATOR / 3
        rect_x2 = rect_x1 + answer / sum(answers) * 100 * PERC_MULTIPLIER
        rect_y2 = y + ROW_SEPARATOR / 3
        color = "red"

        if answer == max(answers):
            color = "green"

        canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, fill=color, outline="")


def add_answer(event=None) -> None:
    key = -1

    match event.keysym:
        case "1":
            key = 0
        case "2":
            key = 1
        case "3":
            key = 2

    if key < 0:
        return

    answers[key] += 1

    display_page(question, answers)

    with open("10-Anketa.txt", "w", encoding="ansi") as f:
        f.write(f"{question}\n")
        f.write(' '.join(str(x) for x in answers))


with open("10-Anketa.txt", "r", encoding="ansi") as f:
    rows = f.readlines()
    question = rows[0].strip()
    answers = [int(x) for x in rows[1].split()]

display_page(question, answers)

root.bind("<Key>", add_answer)
root.mainloop()
