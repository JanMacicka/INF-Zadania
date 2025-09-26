a = int(input("cislo 1: "))
b = int(input("cislo 2: "))
c = int(input("cislo 3: "))

if a <= 0 or b <= 0 or c <= 0:
    print("trojuholnik neexistuje")
    exit()

if a > b:
    a, b = b, a

if a > c:
    a, c = c, a

if b > c:
    b, c = c, b

if a + b <= c or a + c <= b or b + c <= a:
    print("trojuholnik neexistuje")
    exit()

if a == b and a == c:
    print("rovnostranny")
elif a == b or a == c or b == c:
    print("rovnoramenny")
elif c ** 2 == (a **2 + b ** 2):
    print("pravouhly")
else:

    print("roznostranny")
