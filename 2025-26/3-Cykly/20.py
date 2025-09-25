import random

n = int(input("zadaj n: "))
people = 100

for i in range(n):
    boarded = random.randint(0, 9)
    disboarded = random.randint(0, 9)

    print(f"vo vlaku bolo {people} ludi, {boarded} nastupilo, {disboarded} vystupilo, zostalo {people + boarded - disboarded}")

    people = people + boarded - disboarded