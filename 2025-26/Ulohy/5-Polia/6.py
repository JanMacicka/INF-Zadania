numbers = []

for i in range(20):
    numbers.append(input(f"zadajte cislo ({i + 1}.): "))

for number in numbers:
    if numbers.count(number) == 1:
        print(number)