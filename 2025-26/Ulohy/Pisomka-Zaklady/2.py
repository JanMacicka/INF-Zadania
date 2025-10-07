import os

grades = {"SJ": [],
          "AJ": [],
          "NJ": []}

typing = True
all_1 = 0

while typing:
    os.system("cls")

    grade_sj = int(input("zadajte znamku zo SJ: "))
    grade_aj = int(input("zadajte znamku z AJ: "))
    grade_nj = int(input("zadajte znamku z NJ: "))

    if grade_sj + grade_aj + grade_nj == 0:
        break

    if grade_sj == 1 and grade_aj == 1 and grade_nj == 1:
        all_1 += 1

    grades["SJ"].append(grade_sj)
    grades["AJ"].append(grade_aj)
    grades["NJ"].append(grade_nj)

print(f"zo vsetkych 3 predmetov ma 1 {all_1} ziakov.")
print(f"priemer zo SJ: {sum(grades["SJ"]) / len(grades["SJ"])}")
print(f"priemer z AJ: {sum(grades["AJ"]) / len(grades["AJ"])}")
print(f"priemer z NJ: {sum(grades["NJ"]) / len(grades["NJ"])}")