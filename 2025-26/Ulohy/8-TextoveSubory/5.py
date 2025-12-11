text = []

with open("5-1.txt", "r") as f:
    for line in f.readlines():
        text.append(line.strip())

file_1 = []
file_2 = []

for row in text:
    file_1.append(row[::2])
    file_2.append(row[1::2])

with open("5-2.txt", "w") as f:
    f.write("\n".join(" ".join(line for line in file_1)))

with open("5-3.txt", "w") as f:
    f.write("\n".join(" ".join(line for line in file_2)))
    