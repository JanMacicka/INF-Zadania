import random

def print_matrix(matrix):
    for row in matrix:
        print("\t".join(str(_) for _ in row))


rows = int(input("zadajte pocet riadkov: "))
columns = int(input("zadajte pocet stlpcov: "))

matrix = []

for i in range(rows):
    row = [random.randint(1, 10) for _ in range(columns)]

    matrix.append(row)

print_matrix(matrix)

max_value = (0, ())
min_value = (11, ())

for i, row in enumerate(matrix):
    for j, column in enumerate(row):
        if column > max_value[0]:
            max_value = (max(row), (i, j))

        if column < min_value[0]:
            min_value = (min(row), (i, j))

print(min_value)

print(f"maximum: {max_value[0]}, {max_value[1][0] + 1}. riadok, {max_value[1][1] + 1}. stlpec")
print(f"minimum: {min_value[0]}, {min_value[1][0] + 1}. riadok, {min_value[1][1] + 1}. stlpec")

num_sum = 0

for row in matrix:
    num_sum += sum(row)

print(f"sucet:  {num_sum}")

edge_sum = 0

edge_sum += sum(matrix[0]) + sum(matrix[-1])

for row in matrix[1:-1]:
    edge_sum += row[0] + row[-1]

print(f"sucet na obvode: {edge_sum}")

rows_to_swap = input(f"zadajte 2 riadky na vymenu oddelene ciarkou (1-{rows}): ").split(",")

for i, row in enumerate(rows_to_swap):
    rows_to_swap[i] = int(row) - 1

temp_row = matrix[rows_to_swap[0]]
matrix[rows_to_swap[0]] = matrix[rows_to_swap[1]]
matrix[rows_to_swap[1]] = temp_row

print_matrix(matrix)

columns_to_swap = input(f"zadajte 2 stlpce na vymenu oddelene ciarkou (1-{columns}): ").split(",")

for i, column in enumerate(columns_to_swap):
    columns_to_swap[i] = int(column) - 1

for row in matrix:
    temp = row[columns_to_swap[0]]
    row[columns_to_swap[0]] = row[columns_to_swap[1]]
    row[columns_to_swap[1]] = temp

print_matrix(matrix)

diag_sum = 0

for i in range(rows):
    if i > columns - 1:
        break

    diag_sum += matrix[i][i]

print(f"sucet hlavnej diagonaly: {diag_sum}")
