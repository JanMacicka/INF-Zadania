birth_number = input("zadajte rodne cislo: ")

gender = "muz"
diff = 0

if birth_number[2] == "5" or birth_number[2] == "6":
    gender = "otrok"
    diff = 50

year = birth_number[0] + birth_number[1]

if birth_number[0] == "0":
    year = "20" + year
else:
    year = "19" + year

print(f"datum narodenia: {int(birth_number[4] + birth_number[5])}.{int(birth_number[2] + birth_number[3]) - diff}.{year}")
print(f"pohlavie: {gender}")