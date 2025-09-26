a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    print(f"koren 1: {(discriminant ** (1 / 2) - b) / 2 * a}")
    print(f"koren 2: {(discriminant ** (1 / 2) + b) / 2 * a}")
elif discriminant == 0:
    print(f"koren: {- b / 2 * a}")
else:
    print("nema koren v R")