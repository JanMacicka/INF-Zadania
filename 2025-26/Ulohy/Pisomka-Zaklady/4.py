n = int(input("zadajte n: "))
char_1 = input("zadajte znak 1: ")
char_2 = input("zadajte znak 2: ")

for i in range(n):
    if i % 2 == 0:
        print(char_2 * n)
    else:
        print(char_1 * n)