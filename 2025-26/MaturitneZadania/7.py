def main() -> None:
    map = []
    islands = {}

    with open("7-Mapa.txt", "r") as f:
        for row in f.readlines():
            map.append([int(x) for x in row.split()])

    print("mapa:")
    
    for i, row in enumerate(map):
        for j, col in enumerate(row):
            if col != 0:
                print("🟦", end="")

                if col in islands.keys():
                    islands[col].append((i, j))
                else:
                    islands[col] = [(i, j)]
            else:
                print("🟩", end="")

        print()        

    max_area = 0

    for key in islands.keys():
        area = len(islands[key])

        if area > max_area:
            max_area = area

    print(f"pocet ostrovov: {len(islands)}")
    print(f"ostrov s najvacsou nadmorskou vyskou: {max(islands.keys())}")
    print(f"najvacsia rozloha: {max_area}")


if __name__ == "__main__":
    main()
