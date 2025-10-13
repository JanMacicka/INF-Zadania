grades = {}

while True:
    grade = input("zadajte znamku [1-5]: ")

    if grade == "0":
        break
    
    if grade in grades.keys():
        grades[grade] += 1
    else:
        grades[grade] = 1

for grade in grades:
    print(f"{grade}: {grades[grade]}")