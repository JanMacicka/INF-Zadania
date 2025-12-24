import random


def generate_stations(stations: int, days: int) -> list[list[int]]:
    return [[random.randint(-15, 40) for j in range(days)] for i in range(stations)]
    
def average_station_temp(values: list[list[int]]) -> list[int]:
    return [sum(station) / len(station) for station in values]

def average_day_temp(values: list[list[int]]) -> list[int]:
    averages = []

    for i in range(len(values[0])):
        day_sum = 0

        for j in range(len(values)):
            day_sum += values[j][i]

        averages.append(day_sum / len(values))

    return averages

def warmest_day(values: list[list[int]]) -> tuple[int, int, int]:
    warmest_day = (values[0][0], 0, 0)

    for i, station in enumerate(values):
        for j, day in enumerate(station):
            if day > warmest_day[0]:
                warmest_day = (day, i, j)

    return warmest_day

def coldest_day(values: list[list[int]]) -> tuple[int, int, int]:
    coldest_day = (values[0][0], 0, 0)

    for i, station in enumerate(values):
        for j, day in enumerate(station):
            if day < coldest_day[0]:
                coldest_day = (day, i, j)

    return coldest_day

def frozen_days(values: list[list[int]]) -> list[int]:
    counts = []

    for station in values:
        count = 0

        for day in station:
            if day < 0:
                count += 1
        
        counts.append(count)

    return counts

def is_extreme(day: int) -> bool:
    return day >= 35 or day < -10

def dfs(array: list[list[int]], row: int, column: int, visited: list[list[int]]) -> int:
    if row < 0 or row >= len(array) or column < 0 or column >= len(array[0]) or visited[row][column] or not is_extreme(array[row][column]):
        return 0
    
    visited[row][column] = True
    size = 1

    for row_diff, column_diff in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        size += dfs(array, row + row_diff, column + column_diff, visited)

    return size

def find_extreme_areas(array: list[list[int]]) ->list[int]:
    visited = [[False for _ in range(len(array[0]))] for _ in range(len(array))]
    areas = []

    for row in range(len(array)):
        for column in range(len(array[0])):
            if is_extreme(array[row][column]) and not visited[row][column]:
                size = dfs(array, row, column, visited)

                areas.append(size)

    return areas

def main():
    stations = int(input("zadajte pocet stanic: "))
    days = int(input("zadajte pocet dni: "))
    values = generate_stations(stations, days)

    print("St\\Den", end="\t")

    for i in range(days):
        print(i + 1, end="\t")

    for i, station in enumerate(values):
        print(f"\nSt{i + 1}", end="\t")

        for j, day in enumerate(station):
            print(day, end="\t")

    print("\nPriemerne teploty stanic:")

    averages = average_station_temp(values)

    for i, average in enumerate(averages):
        print(f"St{i + 1}: {average}")

    print("Priemerne teploty pre kazdy den:")

    averages = average_day_temp(values)

    for i, average in enumerate(averages):
        print(f"Den {i + 1}: {average}")

    day = warmest_day(values)

    print(f"Nateplejsi den: {day[2] + 1}, stanica: {day[1] + 1}, teplota: {day[0]}")

    day = coldest_day(values)

    print(f"Najchladnejsi den: {day[2] + 1}, stanica: {day[1] + 1}, teplota: {day[0]}")
    print("Pocet dni so zamrznutim podla stanice:")

    frozen = frozen_days(values)

    for i, count in enumerate(frozen):
        print(f"St{i + 1}: {count}")

    print("Extremne oblasti:")

    for i, area in enumerate(find_extreme_areas(values)):
        print(f"{i + 1}. oblast: {area}")


if __name__ == "__main__":
    main()
