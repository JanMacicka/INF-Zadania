import random

num = random.randint(1, 100)
guess = 0
attempts = 0

while guess != num:
    guess = int(input("hadaj cislo: "))
    attempts += 1

    if guess < num:
        print("hladane cislo je vacsie")
    
    if guess > num:
        print("hladane cislo je mensie")

print("uhadnute cislo!")
print(f"pocet pokusov: {attempts}")