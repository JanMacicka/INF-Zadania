numbers = []

for i in range(20):
    numbers.append(input(f"zadajte cislo ({i + 1}.): "))

print(", ".join(sorted(set(numbers))))