class Film:
    def __init__(self, name: str, main_char: str, visits: tuple[int]) -> None:
        self.name = name
        self.main_char = main_char
        self.visits = visits
        self.total_visits = sum(self.visits)

    def __str__(self) -> str:
        return f"{self.name} ({self.main_char}), celkovy pocet navstev: {self.total_visits}"


def sort(films: list[Film]) -> list[Film]:
    return sorted(films, key=lambda x: x.total_visits)[::-1]

def print_best_films(films: list[Film], n=5) -> None:
    print(f"\nNAJLEPSIE FILMY ({n}):")
    print("\n".join(str(film) for film in films[:n]))

def films_by_person(person: str, films: list[Film]) -> None:
    print(f"\nFILMY, KDE HRA {person.upper()}:")
    
    count = 0
    
    for film in films:
        if film.main_char.lower() == person.lower():
            count += 1

            print(film)

    print(f"\npocet: {count}")

def main() -> None:
    films = []

    with open("Filmy.txt", "r") as f:
        for line in f.readlines():
            values = line.split(";")

            films.append(Film(values[0], values[1], tuple([int(x) for x in values[2].split()])))

    films = sort(films)
    count = len(films)

    print("UTRIEDENE FILMY:")
    print("\n".join(str(film) for film in films))
    print(f"\npocet filmov: {count}")
    print_best_films(films)
    films_by_person(input("\nzadajte herca na vyhladanie filmov, v ktorych hra: "), films)


if __name__ == "__main__":
    main()
