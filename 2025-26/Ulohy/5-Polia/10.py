import random

a = [random.randint(0, 100) for _ in range(50)]

print(a)

for i, element in enumerate(a):
    if element % 5 == 0:
        print(i)
        break