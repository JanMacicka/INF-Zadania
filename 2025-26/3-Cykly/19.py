import random

n = int(input("zadaj n: "))

for i in range(n):
    point_1 = random.randint(0, 100)
    point_2 = random.randint(0, 100)

    print(f"prvy bod na priamke: {point_1}, druhy bod: {point_2}, vzdialenost: {abs(point_2 - point_1)}")