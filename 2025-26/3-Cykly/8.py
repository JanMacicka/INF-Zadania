amount = 0

for i in range(1, 1000):
    if i % 5 == 0 and i % 10 != 0:
        amount += 1

print(amount)