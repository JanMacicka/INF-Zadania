a = int(input())
b = int(input())
c = int(input())

max = 0

if a > b:
    max = a
else:
    max = b

if max > c:
    print(max)
else:
    print(c)