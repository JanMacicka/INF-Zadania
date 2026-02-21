import tkinter as tk


WIDTH = 700
HEIGHT = 500

FLAG_WIDTH = 325
FLAG_HEIGHT = 216
OFFSET = 30

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

canvas.create_rectangle(OFFSET, OFFSET, OFFSET + FLAG_WIDTH, OFFSET + FLAG_HEIGHT / 3, outline="")
canvas.create_rectangle(OFFSET, OFFSET + FLAG_HEIGHT / 3, OFFSET + FLAG_WIDTH, OFFSET + 2 * FLAG_HEIGHT / 3, fill="#0b4ea2", outline="")
canvas.create_rectangle(OFFSET, OFFSET + 2 * FLAG_HEIGHT / 3, OFFSET + FLAG_WIDTH, OFFSET + FLAG_HEIGHT, fill="#ee1c25", outline="")

image = tk.PhotoImage(file="21-1.png")

canvas.create_image(OFFSET + 100, OFFSET + 108, image=image)
canvas.create_rectangle(OFFSET, OFFSET, OFFSET + FLAG_WIDTH, OFFSET + FLAG_HEIGHT)
    
root.mainloop()
