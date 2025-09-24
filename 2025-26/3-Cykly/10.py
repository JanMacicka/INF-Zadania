import os
import random

amount = int(input("zadajte pocet prikladov: "))
points = 0

for i in range(amount):
    os.system("cls")

    num_1 = random.randint(0, 10)
    num_2 = random.randint(0, 10)

    result = int(input(f"{num_1}*{num_2}: "))

    if result == num_1 * num_2:
        print("spravne")
        points += 1
    else:
        print("nespravne")

    input("pre pokracovanie stlacte akykolvek klaves")

print(f"vysledok: {points / amount * 100}%")