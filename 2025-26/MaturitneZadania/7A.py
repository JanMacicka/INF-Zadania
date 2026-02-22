from collections import deque


class Field:
    def __init__(self, value: int) -> None:
        self.value = value
        self.visited = False
        self.neighbors = []


    def is_island(self) -> bool:
        return self.value > 0


class Island:
    def __init__(self) -> None:
        self.__fields = []
        self.height = 0
        self.area = 0


    def __str__(self) -> str:
        return f"rozloha: {self.area}, vyska: {self.height}"


    def add_field(self, field: Field) -> None:
        self.__fields.append(field)

        self.area += 1


class Map:
    def __init__(self) -> None:
        self.fields = []


    def __connect_island_fields(self, field_1: Field, field_2: Field) -> None:
        if field_1.value == field_2.value and field_2 not in field_1.neighbors:
            field_1.neighbors.append(field_2)
            field_2.neighbors.append(field_1)


    def bfs(self, field: Field) -> Island:
        field.visited = True
        queue = deque()
        island = Island()

        queue.append(field)

        while queue:
            current = queue.popleft()

            island.add_field(current)

            island.height = current.value

            for field in current.neighbors:
                if not field.visited:
                    field.visited = True

                    queue.append(field)

        return island


    def calculate_neighbors(self) -> None:
        for i, row in enumerate(self.fields):
            for j, field in enumerate(row):
                if not field.is_island():
                    continue

                if j > 0: # left neighbor
                    self.__connect_island_fields(field, row[j - 1])

                if j < len(row) - 1: #right neighbor
                    self.__connect_island_fields(field, row[j + 1])

                if i > 0: #top neighbor
                    self.__connect_island_fields(field, self.fields[i - 1][j])

                if i < len(self.fields) - 1: # bottom neighbor
                    self.__connect_island_fields(field, self.fields[i + 1][j])

        
    def get_islands(self) -> list[Island]:
        islands = []

        for row in self.fields:
            for field in row:
                if not field.is_island() or field.visited:
                    continue

                islands.append(self.bfs(field))

        return islands


def main() -> None:
    map = Map()

    with open("7-Mapa.txt", "r") as f:
        for row in f.readlines():
            map.fields.append([Field(int(x)) for x in row.split()])

    map.calculate_neighbors()
    
    islands = map.get_islands()
    islands = sorted(islands, key=lambda i: i.area, reverse=True)

    print(f"pocet ostrovov: {len(islands)}")
    print(f"ostrov s najvacsou rozlohou: {islands[0]}")

    islands = sorted(islands, key=lambda i: i.height, reverse=True)

    print(f"ostrov s najvacsou nadmorskou vyskou: {islands[0]}")

    print("mapa:")

    for row in map.fields:
        for field in row:
            if field.value == 0:
                print("🟦", end="")
            else:
                print("🟩", end="")

        print()

        
if __name__ == "__main__":
    main()
