import os

class Book:
    def __init__(self, author: str, title: str, publisher: str, year: int, price: float) -> None:
        self.author = author
        self.title = title
        self.publisher = publisher
        self.year = year
        self.price = price

    def __str__(self) -> str:
        return f"{self.author}: {self.title} ({self.publisher}, {self.year}), cena: {str(self.price).replace('.', ',')} €"

    
def print_books(books: list[Book]) -> None:
    print("\n".join(str(book) for book in books))
    print(f"pocet najdenych zaznamov: {len(books)}")
    input("stlacte enter pre pokracovanie.")

def main() -> None:
    books = []

    with open("7.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            book = line.split(";")

            books.append(Book(book[0], book[1], book[2], int(book[3]), float(book[4])))

    typing = True

    while typing:
        os.system("cls")
        choice = input("zadajte, co chcete vyhladat [a - hladanie podla autora, c - hladanie podla ceny, v - hladanie podla vydavatelstva a roku vydania, enter - ukoncenie]: ")

        match choice:
            case "a":
                author = input("zadajte meno autora: ").lower()
                books_to_print = [book for book in books if book.author.lower() == author]
            case "c":
                price = [float(x) for x in input("zadajte cenove ohranicenie (spodnu a hornu hranicu oddelte ciarkou): ").split(",")]
                min_price, max_price = min(price), max(price)
                books_to_print = [book for book in books if book.price > min_price and book.price <= max_price]
            case "v":
                publisher = input("zadajte vydavatelstvo: ").lower()
                year = int(input("zadajte rok vydania: "))
                books_to_print = [book for book in books if book.publisher.lower() == publisher and book.year == year]
            case _:
                typing = False

        if len(books_to_print) > 0:
            print_books(books_to_print)


if __name__ == "__main__":
    main()
