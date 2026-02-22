import math
import random


def main() -> None:
    text = input("zadajte text na zasifrovanie: ")
    matrix = [[] for _ in range(math.ceil(math.sqrt(len(text))))]
    size = len(matrix)

    for i, char in enumerate(text):
        matrix[i % size].append(char)

    for col in matrix:
        if col == []:
            matrix.remove(col)

    for i in range(random.randint(1, size)):
        col_1 = random.randint(0, size - 1)
        col_2 = random.randint(0, size - 1)

        temp = matrix[col_1]
        matrix[col_1] = matrix[col_2]
        matrix[col_2] = temp

    print("zasifrovany text:")

    for i in range(size):
        for j in range(size):
            if i >= len(matrix[j]):
                break

            print(matrix[j][i], end="\t")

        print()


if __name__ == "__main__":
    main()
