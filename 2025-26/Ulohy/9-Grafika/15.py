import tkinter as tk


WIDTH = 700
HEIGHT = 500

FLAG_WIDTH = 300
FLAG_HEIGHT = 200
OFFSET = 50, 50

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

canvas.create_rectangle(OFFSET[0], OFFSET[1], OFFSET[0] + FLAG_WIDTH, OFFSET[1] + FLAG_HEIGHT / 2, outline="")
canvas.create_rectangle(OFFSET[0], OFFSET[1] + FLAG_HEIGHT / 2, OFFSET[0] + FLAG_WIDTH, OFFSET[1] + FLAG_HEIGHT, fill="red", outline="")
canvas.create_polygon(OFFSET[0], OFFSET[1], OFFSET[0], OFFSET[1] + FLAG_HEIGHT, OFFSET[0] + FLAG_WIDTH / 2, OFFSET[1] + FLAG_HEIGHT / 2, fill="dark blue", outline="")
canvas.create_rectangle(OFFSET[0], OFFSET[1], OFFSET[0] + FLAG_WIDTH, OFFSET[1] + FLAG_HEIGHT, fill="", outline="black", width=2)
    
root.mainloop()
