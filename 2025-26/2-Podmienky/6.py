days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum = 0

day = int(input("zadajte den: "))

for i in range(len(days) - 1):
    sum += days[i]

    if day > sum and day <= sum + days[i + 1]:
        days_in_month = day - sum

        print(f"{days_in_month}.{i + 2}.")
        break