n = int(input("zadaj cislo: "))

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1

    if n != 1:
        print(n, end=", ")
    else:
        print(n)