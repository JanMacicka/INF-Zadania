import tkinter as tk


WINDOW_WIDTH = 400
WINDOW_HEIGHT = 425
PIXEL_MULTIPLIER = 4

root = tk.Tk()
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

canvas.pack()

dimensions = ()
count_1 = 0
matrix = []


def generate_view(matrix=matrix) -> None:
    canvas.delete("all")

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            x1 = j * PIXEL_MULTIPLIER
            y1 = i * PIXEL_MULTIPLIER
            x2 = x1 + PIXEL_MULTIPLIER
            y2 = y1 + PIXEL_MULTIPLIER

            if col == "1":
                canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="")

    button = tk.Button(root, text="Preklopit", command=swap)

    button.place(x=WINDOW_WIDTH / 2, y=WINDOW_HEIGHT, anchor="s")


def swap() -> None:
    global matrix

    matrix = [x[::-1] for x in matrix]

    generate_view(matrix=matrix)


with open("26-PreklopenieObrazka.txt", "r") as f:
    dimensions = tuple([int(x) for x in f.readline().split()])

    for row in f.readlines():
        matrix.append([])

        for char in row.split():
            matrix[-1].append(char)

            if char == "1":
                count_1 += 1

print(f"pocet pixelov: {dimensions[0] * dimensions[1]}")
print(f"pocet jednotiek: {count_1}")
generate_view()

root.mainloop()
