income = int(input("povodne vreckove: "))
diff = int(input("tyzdenne zvysenie vreckoveho: "))

result = 0

for i in range(52):
    result += income
    result += diff

print(f"vyplati: {result}")