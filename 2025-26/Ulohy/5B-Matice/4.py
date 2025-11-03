import random

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(_) for _ in row))


temps = []
YEARS = 10
DAYS = 365

for i in range(YEARS):
    year = [random.randint(-30, 40) for _ in range(DAYS)]

    temps.append(year)

print("TEPLOTY:")
print_matrix(temps)

averages = []
max_temp = temps[0][0]
min_temp = temps[0][0]

for i in range(DAYS):
    day_sum = 0

    for j in range(YEARS):
        temp = temps[j][i]
        day_sum += temp

        if max_temp < temp:
            max_temp = temp
        
        if min_temp > temp:
            min_temp = temp

    averages.append(day_sum / YEARS)

for i, value in enumerate(averages):
    print(f"priemerna teplota pre {i + 1}. den za poslednych {YEARS} rokov: {value}")

print(f"najvyssia teplota: {max_temp}")
print(f"najnizsia teplota: {min_temp}")