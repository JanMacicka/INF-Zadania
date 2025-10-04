min = 11
max = 0
count = 0
sum = 0

while True:
    grade = int(input("zadajte znamku (1 - 10): "))

    if grade == 0:
        break
    
    count += 1
    sum += grade

    if max < grade:
        max = grade

    if min > grade:
        min = grade

print(f"vysledok: {(sum - min - max) / (count - 2)}")