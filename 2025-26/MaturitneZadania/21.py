import os


def get_entries() -> dict[str, int]:
    entries = {}

    with open("21-Pokuty.txt", "r", encoding="utf-8") as f:
        for row in f.readlines():
            values = row.split()
            entries[values[0]] = int(values[1])

    return entries


def set_entries(entries: dict[str, int]) -> None:
    with open("21-Pokuty.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(f"{key} {value}" for key, value in entries.items()))


def main() -> None:
    while True:
        os.system("cls")
        print("POKUTY")

        entries = get_entries()
        driver = input("Zadajte vodica na udelenie / zaplatenie pokuty: ")
        fine_price = int(input("Zadajte vysku pokuty: "))

        if driver in entries.keys():
            entries[driver] += fine_price

            if entries[driver] <= 0:
                entries.pop(driver)
        else:
            entries[driver] = fine_price

        set_entries(entries)
        input("Udaje boli upravene. Stlacte akykolvek klaves pre pokracovanie. ")


if __name__ == "__main__":
    main()
