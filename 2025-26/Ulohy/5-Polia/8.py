import os
import random

money = int(input("servus, ty milovnik ovocicka, zadaj svoj vklad: "))
numbers = [random.randint(1, 99) for _ in range(10)]
correct = 0
win_multiplier = 1

for i in range(10):
    os.system("cls")
    
    guess = int(input("hadaj [1-10]: "))

    if guess in numbers:
        correct += 1

        numbers.remove(guess)

os.system("cls")

match correct:
    case 10:
        win_multiplier = 200000
    case 9:
        win_multiplier = 10000
    case 8:
        win_multiplier = 500
    case 7:
        win_multiplier = 20
    case 6:
        win_multiplier = 10
    case 5:
        win_multiplier = 3

print(f"vyhral si {money * win_multiplier} €. uhadol si {correct} cisel.")
