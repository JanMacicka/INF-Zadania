from datetime import datetime, timedelta


YEAR = 2026
TODAY = datetime(year=YEAR, month=12, day=24)
BORROW_LIMIT = 30


class Borrow:
    def __get_borrow_time(self) -> timedelta:
        date_to = self.date_to

        if date_to is None:
            date_to = TODAY

        return date_to - self.date_from
    

    def __is_in_limit(self) -> bool:
        return self.borrowed_time < timedelta(days=BORROW_LIMIT)
    

    def __init__(self, date_from: datetime, date_to: datetime | None) -> None:
        self.date_from = date_from
        self.date_to = date_to
        self.borrowed_time = self.__get_borrow_time()
        self.in_limit = self.__is_in_limit()


class Book:
    def __get_total_borrow_time(self) -> datetime:
        borrow_sum = timedelta(days=0)

        for borrow in self.borrows:
            borrow_sum += borrow.borrowed_time

        return borrow_sum
    

    def __init__(self, name: str, borrows: list[Borrow]) -> None:
        self.name = name
        self.borrows = borrows
        self.total_borrow_time = self.__get_total_borrow_time()


    def __str__(self) -> str:
        return f"{self.name}"
    

def main() -> None:
    books = []

    with open("17-Knihy.txt", "r") as f:
        rows = f.readlines()

        for i in range(0, len(rows) - 1, 2):
            name = rows[i].strip()
            dates = rows[i + 1].split()
            dates = [((int(dates[i][2:]), int(dates[i][:2])), ((int(dates[i + 1][2:]), int(dates[i + 1][:2])) if i + 1 < len(dates) else None)) for i in range(0, len(dates), 2)]
            borrows = []

            for date_pair in dates:
                date_from = datetime(year=YEAR, month=date_pair[0][0], day=date_pair[0][1])
                date_to = None

                if date_pair[1] is not None:
                    date_to = datetime(year=YEAR, month=date_pair[1][0], day=date_pair[1][1])

                borrows.append(Borrow(date_from, date_to))

            books.append(Book(name, borrows))

    books = sorted(books, key=lambda b: len(b.borrows), reverse=True)
    most_borrowed_book = None

    print("knihy, na ktore treba poslat upomienku:")

    for book in books:
        if len(book.borrows) > 0 and not book.borrows[-1].in_limit:
            print(book)

        if most_borrowed_book is None or len(book.borrows) > len(most_borrowed_book.borrows):
            most_borrowed_book = book

    print(f"najpoziciavanejsia kniha: {most_borrowed_book}")
    print("zoradene knihy podla dlzky doby vypozicania:")

    for book in books:
        print(book)


if __name__ == "__main__":
    main()
