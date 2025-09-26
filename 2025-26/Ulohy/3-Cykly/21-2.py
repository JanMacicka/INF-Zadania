n = int(input("zadaj n: "))

for i in range(n):
    for j in range(3):
        for k in range(n):
            print(f"{i * n + k + 1 :2}", end=" ")

        print("    ", end="")

    print()