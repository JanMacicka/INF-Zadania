num = input("zadaj cislo: ")
sum = 0

for position in num:
    sum += int(position)

    print(f"cifra {position}")

print(f"ciferny sucet: {sum}")