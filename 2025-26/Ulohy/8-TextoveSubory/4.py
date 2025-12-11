text = []

with open("4-1.txt", "r") as f:
    for line in f.readlines():
        new_line = line.strip()[::-1]
        
        if new_line[0] == ".":
            new_line = new_line[1:]
            new_line += "."

        if new_line[0] == ",":
            new_line = new_line[1:]
            new_line += ","

        text.append(new_line)

with open("4-2.txt", "w") as f:
    f.write("\n".join(text))
