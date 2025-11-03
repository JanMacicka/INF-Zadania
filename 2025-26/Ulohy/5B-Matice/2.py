import random

def print_matrix(matrix):
    for row in matrix:
        print("\t".join(str(_) for _ in row))


rows = int(input("zadajte pocet riadkov: "))
columns = int(input("zadajte pocet stlpcov: "))

matrices = []

for i in range(2):
    matrices.append([])

    for j in range(rows):
        row = [random.randint(1, 10) for _ in range(columns)]

        matrices[i].append(row)

print_matrix(matrices[0])
print()
print_matrix(matrices[1])

sum_matrix = []

for i in range(rows):
    sum_matrix.append([])

    for j in range(columns):
        sum_matrix[i].append(matrices[0][i][j] + matrices[0][i][j])

print("\nSUCET:")
print_matrix(sum_matrix)
