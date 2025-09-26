import random

rolls = int(input("pocet hodov: "))
dice = int(input("pocet kociek: "))

for i in range(rolls):
    sum = 0

    for j in range(dice):
        num = random.randint(1, 6)
        sum += num

        print(f"na {j + 1}. kocke padla {num}")

    print(f"ich sucet je {sum}")
    print()