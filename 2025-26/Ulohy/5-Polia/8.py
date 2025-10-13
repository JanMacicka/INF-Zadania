import os
import random

money = int(input("servus, ty milovnik ovocicka, zadaj svoj vklad: "))
correct = 0
win = 1

for i in range(10):
    os.system("cls")

    num = random.randint(0, 10)
    guess = int(input("hadaj [1-10]: "))

    if num == guess:
        correct += 1

os.system("cls")

match correct:
    case 10:
        win = 200000
    case 9:
        win = 10000
    case 8:
        win = 500
    case 7:
        win = 20
    case 6:
        win = 10
    case 5:
        win = 3

print(f"vyhral si {money * win} €. uhadol si {correct} cisel.")