class Town:
    def __init__(self, id: int) -> None:
        self.id = id


class Road:
    def __init__(self, towns: list[Town], length: int) -> None:
        self.towns = towns
        self.length = length


def main() -> None:
    lengths = []
    roads = []

    with open("27-Cesty.txt", "r") as f:
        for row in f.readlines():
            lengths.append([int(x) for x in row.split()])

    for i in range(len(lengths) - 1):
        for j in range(i + 1, len(lengths[i])):
            if lengths[i][j] != 0:
                roads.append(Road([i, j], lengths[i][j]))

    total_length = 0

    for road in roads:
        total_length += road.length

    print(f"celkova dlzka cestnej siete: {total_length}")

    roads = sorted(roads, key= lambda r: r.length, reverse=True)

    print(f"najvzdialenejsie mesta: {" a ".join(str(t + 1) for t in roads[0].towns)}")

if __name__ == "__main__":
    main()
