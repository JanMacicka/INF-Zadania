import random

def print_matrix(array: list[list[int]]) -> None:
    """
    vypise maticu
    """

    for value in array:
        print("  ".join(str(_) for _ in value))

def is_continous(array: list[list[int]]) -> bool:
    """
    zisti, ci je matica suvisla
    """

    problems = []

    for i in range(len(array)):
        for j in range(i + 1, len(array)): # iterujeme iba cez "trojuholnik"
            if array[i][j] == 0:
                problems.append((i, j))
            
    if not problems:
        return True
    
    for problem in problems:
        i = problem[0]
        j = problem[1]

    # vzhladom na nedostatok casu opisem postup, ako by som pokracoval:
    # - implementujem BFS (hladanie grafu do sirky) algoritmus, ktorym by som postupne vyhladaval v grafe a hladal cesty
    # - ak sa najdu vsetky cesty, mozeme konstatovat, ze graf je suvisly
    # - idealne by bolo v takomto pripade reprezentovat jednotlive uzly grafu ako objekty a potom sa na BFS realizovat napriklad cez zoznam susedov a nie maticu, matica je aj tak reduntantna
    # - prijemne citanie :D

city_count = int(input("zadajte pocet miest: "))
# inicializujeme nulovu maticu
roads = [[0 for j in range(city_count)] for i in range(city_count)]
for i in range(city_count):
    for j in range(city_count):
        if i == j:
            continue

        distance = random.randint(0, 100)
        roads[i][j], roads[j][i] = distance, distance

print_matrix(roads)

# inicializujeme premenne na vypocet najkratsej nenulovej vzdialenosti:
min_distance = (100, ())

for i in range(city_count):
    for j in range(i + 1, city_count):
        if roads[i][j] != 0 and roads[i][j] < min_distance[0]:
            min_distance = roads[i][j], (i, j)

print(f"najkratsia existujuca trasa je medzi mestami {min_distance[1][0] + 1} a {min_distance[1][1] + 1}")

# zistime sucty dlzok spojeni
sums = [0 for _ in range(city_count)]

for i in range(city_count):
    for j in range(city_count):
        sums[i] += roads[i][j]

# vypocitame maximalnu dlzku z 1 mesta
best = sums[0], 0

for index, value in enumerate(sums):
    if value > best[0]:
        best = sums[index], index

print("sucty pre jednotlive mesta: ")
print(", ".join(str(sum) for sum in sums))
print(f"najlepsie mesto: {best[1] + 1}.")

# inicializujeme hodnoty na vymenu
cities_to_swap = input(f"zadajte 2 mesta na vymenu oddelene ciarkou (interval 1 - {city_count}): ").split(",")
city_1 = int(cities_to_swap[0]) - 1
city_2 = int(cities_to_swap[1]) - 1

roads[city_1], roads[city_2] = roads[city_2], roads[city_1] # prehodime riadky

for i in range(city_count):
    roads[i][city_1], roads[i][city_2] = roads[i][city_2], roads[i][city_1] # prehodime stlpce

print("cesty po prehodeni miest:")
print_matrix(roads)

# zistime suvislost matice
if is_continous(roads):
    print("siet je suvisla")
else:
    print("siet nie je suvisla")
