import random

previous = 0
repetitions = 0

for i in range(1000):
    current = random.randint(1, 6)

    if current == 6 and previous == 6:
        repetitions += 1

    previous = current

print(f"pocet opakovani hodu 6: {repetitions}")