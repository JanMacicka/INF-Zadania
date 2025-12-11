text = []

with open("3.txt", "r") as f:
    for line in f.readlines():
        text.append(line.split())

longest = (0, "")
lengths = {}

for row in text:
    for word in row:
        length = len(word)

        if length > longest[0]:
            longest = (length, word)

        if length in lengths:
            lengths[length] += 1
        else:
            lengths[length] = 1

print(f"najdlhsie slovo: {longest[1]} - {longest[0]} znakov")

for entry in lengths:
    print(f"{entry} znakov: {lengths[entry]}")
