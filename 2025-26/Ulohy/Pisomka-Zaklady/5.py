import random

limit = int(input("zadajte hranicu: "))
n = int(input("zadajte n: "))

for i in range(n):
    row_sum = 0

    while row_sum < limit:
        num = random.randint(1, 4)
        row_sum += num

        print(num, end=" ")

    if row_sum == limit:
        print("HURA")
    else:
        print("SKODA")