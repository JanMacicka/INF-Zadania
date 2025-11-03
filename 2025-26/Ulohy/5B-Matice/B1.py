import random

def print_matrix(matrix):
    for row in matrix:
        print("\t".join(str(_) for _ in row))


ROWS = 5
COLUMNS = 4

matrix = []

for i in range(ROWS):
    row = [random.randint(1, 10) for _ in range(COLUMNS)]

    matrix.append(row)

print_matrix(matrix)

new_matrix = []

for i in range(COLUMNS - 1, -1, -1):
    new_row = []

    for j in range(ROWS):
        new_row.append(matrix[j][i])

    new_matrix.append(new_row)

print("matica otocena o 90 st. dolava:")
print_matrix(new_matrix)
