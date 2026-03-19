import tkinter as tk


class Char:
    def __init__(self, value: str, level=0) -> None:
        self.value = value
        self.level = level

    
    def __str__(self) -> str:
        return self.value


WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
MARGIN = 10
CHAR_MARGIN = 13

colors = ["dark violet", "blue", "deep sky blue", "green", "yellow", "orange", "red"]
text = input("zadajte vyraz na kontrolu uzatvorkovania: ")
level = 0
chars = []
correct = True

if text.count("(") != text.count(")"):
    correct = False

for char in text:
    if char == "(":
        level += 1
        
        chars.append(Char(char, level))
    elif char == ")":
        if level == 0:
            correct = False

        chars.append(Char(char, level))

        level -= 1
    else:
        chars.append(Char(char))

if level != 0:
    correct = False

root = tk.Tk()
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

canvas.pack()

for i, char in enumerate(chars):
    color = "black"

    if correct and char.level != 0:
        color = colors[char.level % len(colors)]

    canvas.create_text(MARGIN + CHAR_MARGIN * i, MARGIN, anchor="nw", text=str(char), fill=color, font="Consolas 20")

reply = "uzatvorkovanie nie je spravne"

if correct:
    reply = "uzatvorkovanie je spravne"

canvas.create_text(MARGIN, MARGIN + 30, anchor="nw", text=reply, font="Consolas 20")

root.mainloop()
