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

const = int(input("zadajte konstantu na vynasobenie: "))
new_matrix = []

for row in matrix:
    new_matrix.append([])
    for column in row:
        new_matrix[-1].append(column * const)

print_matrix(new_matrix)
