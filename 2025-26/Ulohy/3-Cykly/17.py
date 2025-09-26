def set_width(num, max_size):
    return " " * (max_size - len(str(num))) + str(num) 

COLUMNS = 4

values = []
sizes = []

num_from = int(input("od: "))
num_to = int(input("do: "))

for i in range(num_to - num_from + 1):

    values.append([])

    for j in range(COLUMNS):
        values[i].append((num_from + i) ** (j + 1))

for num in values[-1]:
    sizes.append(len(str(num)))

for i, row in enumerate(values):
    for j, num in enumerate(row):
        values[i][j] = set_width(values[i][j], sizes[j])

    print(*row)