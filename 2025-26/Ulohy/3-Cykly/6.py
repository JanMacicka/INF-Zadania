import random

amount = 0

for i in range(1000):
    num_1 = random.randint(1, 6)
    num_2 = random.randint(1, 6)

    if num_1 == num_2:
        amount += 1

print(f"pravdepodobnost: {amount / 1000}")