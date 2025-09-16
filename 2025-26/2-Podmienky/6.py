days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum = 0

day = int(input("zadajte den: "))

for i in range(len(days) - 1):
    sum += days[i]

    if day > sum:
        print(f"{day - sum}.{i + 2}.")
        break
