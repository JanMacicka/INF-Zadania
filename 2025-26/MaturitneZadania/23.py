import tkinter as tk


WINDOW_WIDTH = 512
WINDOW_HEIGHT = 500
COL_WIDTH = 2

root = tk.Tk()
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

canvas.pack()

dimensions = ()
colors = {x: 0 for x in range(256)}

with open("23-CiernobielyObrazok-1.txt", "r") as f:
    dimensions = tuple([int(x) for x in f.readline().split()])
    
    for row in f.readlines():
        for i in range(0, len(row) - 1, 2):
            value = int(row[i] + row[i + 1], 16)
            colors[value] += 1

max_color = max(colors, key=colors.get)

print(f"sirka: {dimensions[0]}, vyska: {dimensions[1]}, pocet bodov: {dimensions[0] * dimensions[1]}")
print(f"najcastejsie pouzity odtien: {max_color:x}, pocet vyskytov: {colors[max_color]}")

for color in sorted(colors):
    x1 = color * COL_WIDTH
    x2 = x1 + COL_WIDTH
    y1 = WINDOW_HEIGHT
    y2 = WINDOW_HEIGHT - colors[color] / colors[max_color] * WINDOW_HEIGHT

    canvas.create_rectangle(x1, y1, x2, y2, fill="grey", outline="")

root.mainloop()
