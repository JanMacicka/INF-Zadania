import tkinter as tk


WIDTH = 700
HEIGHT = 500
X_OFFSET = 20
Y_OFFSET = 20
MARGIN = 30
FLAG_WIDTH = 135
FLAG_HEIGHT = 90
OUTLINE_WIDTH = 2

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")

canvas.pack()

# DE:
canvas.create_rectangle(X_OFFSET, Y_OFFSET, X_OFFSET + FLAG_WIDTH, Y_OFFSET + FLAG_HEIGHT / 3, fill="black", outline="")
canvas.create_rectangle(X_OFFSET, Y_OFFSET + FLAG_HEIGHT / 3, X_OFFSET + FLAG_WIDTH, Y_OFFSET + FLAG_HEIGHT * 2 / 3, fill="red", outline="")
canvas.create_rectangle(X_OFFSET, Y_OFFSET + FLAG_HEIGHT * 2 / 3, X_OFFSET + FLAG_WIDTH, Y_OFFSET + FLAG_HEIGHT, fill="yellow", outline="")
canvas.create_rectangle(X_OFFSET, Y_OFFSET, X_OFFSET + FLAG_WIDTH, Y_OFFSET + FLAG_HEIGHT, width=OUTLINE_WIDTH, fill="", outline="black")

flag_1_end = (X_OFFSET + FLAG_WIDTH + MARGIN, Y_OFFSET + FLAG_HEIGHT + MARGIN)

# IT:
canvas.create_rectangle(flag_1_end[0], Y_OFFSET, flag_1_end[0] + FLAG_WIDTH / 3, Y_OFFSET + FLAG_HEIGHT, fill="dark green", outline="")
canvas.create_rectangle(flag_1_end[0] + FLAG_WIDTH / 3, Y_OFFSET, flag_1_end[0] + FLAG_WIDTH * 2 / 3, Y_OFFSET + FLAG_HEIGHT, fill="white", outline="")
canvas.create_rectangle(flag_1_end[0] + FLAG_WIDTH * 2 / 3, Y_OFFSET, flag_1_end[0] + FLAG_WIDTH, Y_OFFSET + FLAG_HEIGHT, fill="red", outline="")
canvas.create_rectangle(flag_1_end[0], Y_OFFSET, flag_1_end[0] + FLAG_WIDTH, Y_OFFSET + FLAG_HEIGHT, width=OUTLINE_WIDTH, fill="", outline="black")

# FR:
canvas.create_rectangle(X_OFFSET, flag_1_end[1], X_OFFSET + FLAG_WIDTH / 3, flag_1_end[1] + FLAG_HEIGHT, fill="blue", outline="")
canvas.create_rectangle(X_OFFSET + FLAG_WIDTH / 3, flag_1_end[1], X_OFFSET + FLAG_WIDTH * 2 / 3, flag_1_end[1] + FLAG_HEIGHT, fill="white", outline="")
canvas.create_rectangle(X_OFFSET + FLAG_WIDTH * 2 / 3, flag_1_end[1], X_OFFSET + FLAG_WIDTH, flag_1_end[1] + FLAG_HEIGHT, fill="red", outline="")
canvas.create_rectangle(X_OFFSET, flag_1_end[1], X_OFFSET + FLAG_WIDTH, flag_1_end[1] + FLAG_HEIGHT, width=OUTLINE_WIDTH, fill="", outline="black")

# UA:
canvas.create_rectangle(flag_1_end[0], flag_1_end[1], flag_1_end[0] + FLAG_WIDTH, flag_1_end[1] + FLAG_HEIGHT / 2, fill="dodger blue", outline="")
canvas.create_rectangle(flag_1_end[0], flag_1_end[1] + FLAG_HEIGHT / 2, flag_1_end[0] + FLAG_WIDTH, flag_1_end[1] + FLAG_HEIGHT, fill="yellow", outline="")
canvas.create_rectangle(flag_1_end[0], flag_1_end[1], flag_1_end[0] + FLAG_WIDTH, flag_1_end[1] + FLAG_HEIGHT, width=OUTLINE_WIDTH, fill="", outline="black")

root.mainloop()
