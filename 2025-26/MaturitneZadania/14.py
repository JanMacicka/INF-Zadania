import tkinter as tk


WINDOW_WIDTH = 480
WINDOW_HEIGHT = 520

root = tk.Tk()
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

canvas.pack()

reviews_by_hour = {x: 0 for x in range(24)}

with open("14-Spokojnost.txt", "r", encoding="ansi") as f:
    for row in f.readlines():
        values = row.split()

        if values[1] == "áno":
            continue

        time = [int(x) for x in values[0].split(":")]
        reviews_by_hour[time[0]] += 1

worst_hour = 0

print(f"pocet negativnych vyjadreni: {sum(reviews_by_hour.values())}")
print("hodiny s negativnymi vyjadreniami:")

for hour in reviews_by_hour:
    review_count = reviews_by_hour[hour]

    if review_count > reviews_by_hour[worst_hour]:
        worst_hour = hour

    if review_count > 0:
        print(f"{hour}. - {reviews_by_hour[hour]} negativnych hodnoteni")

    # tkinter

print(f"najhorsia hodina: {worst_hour}. - {reviews_by_hour[worst_hour]} negativnych hodnoteni")

root.mainloop()
