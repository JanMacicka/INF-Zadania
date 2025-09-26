m = int(input("zadajte cislo (< 18): "))

if m >= 18:
    print("cislo musi byt mensie ako 18")
    exit()

for i in range(1, 10):
    for j in range(10):
        if i + j == m:
            print(str(i) + str(j))