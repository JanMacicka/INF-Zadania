amount = 0

for i in range(1, 1000):
    for j in str(i):
        if j == "5":
            amount += 1

print(amount)
