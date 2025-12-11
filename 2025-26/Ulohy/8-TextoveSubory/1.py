nums = []

with open("1-1.txt", "r") as f:
    nums = f.readline().split()

powers = [str(int(_) ** 2) for _ in nums]

print("druhe mocniny:")
print(", ".join(powers))

with open("1-2.txt", "w") as f:
    f.write(" ".join(powers))

with open("1-1.txt", "a") as f:
    f.write(" ".join(powers))
