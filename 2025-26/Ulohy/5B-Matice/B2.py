def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(_) for _ in row))

    print()


n = int(input("zadajte N: "))

matrix_diag = [[0] * n for _ in range(n)]

current_num = 0

for sum in range(2 * n - 1):
    for i in range(n):
        j = sum - i

        if j >= 0 and j < n:
            current_num += 1

            matrix_diag[i][j] = current_num

print_matrix(matrix_diag)

matrix_snail = [[0] * n for _ in range(n)]

row, col, current_num = -1, 0, 0

while current_num < n ** 2:
    while row < n - 1 and matrix_snail[row + 1][col] == 0:
        current_num += 1
        row += 1
        matrix_snail[row][col] = current_num

    while col < n - 1 and matrix_snail[row][col + 1] == 0:
        current_num += 1
        col += 1
        matrix_snail[row][col] = current_num

    while row > 0 and matrix_snail[row - 1][col] == 0:
        current_num += 1
        row -= 1
        matrix_snail[row][col] = current_num

    while col > 0 and matrix_snail[row][col - 1] == 0:
        current_num += 1
        col -= 1
        matrix_snail[row][col] = current_num

print_matrix(matrix_snail)
