n = int(input("zadajte pocet clenov: "))

result = 4

for i in range(n - 1):
    value = 4 / (2 * i + 3)

    if i % 2 == 0:
        result -= value
    else:
        result += value

print(f"pi = {result}")