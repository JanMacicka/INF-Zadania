import random


def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]


amount = int(input("zadajte pocet cisel: "))
numbers = [random.randint(0, 1001) for _ in range(amount)]

for number in numbers:
    if is_palindrome(number):
        print("\033[91m" + str(number) + "\033[0m")
    else:
        print(number)

coef = int(input("zadajte koeficient palindromu: "))

with open("2-Palindromy.txt", "w") as f:
    for i in range(coef):
        for j in range(1, 10):
            f.write(f"{str(j)}{str(i)}{str(j)}\n")
