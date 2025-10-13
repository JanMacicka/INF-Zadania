import random

a = sorted([random.randint(1, 100) for _ in range(10)])
b = sorted([random.randint(1, 100) for _ in range(10)])

print(sorted(a + b))