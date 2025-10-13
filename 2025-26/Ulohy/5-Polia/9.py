import random

a = [random.randint(0, 10) for _ in range(10)]
indices = []

for i, element in enumerate(a):
    greater = True

    for j, num in enumerate(a[i + 1:]):
        if num >= element:
            greater = False

    if greater:
        indices.append(i)

print(a)
print(", ".join([str(x) for x in indices]))