class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f"{self.day}.{self.month}.{self.year}"

class Person:
    def __init__(self, name: str, surname: str, birth_date: Date) -> None:
        self.name = name
        self.surname = surname
        self.birth_date = birth_date

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"


people = []

with open("6.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        person = line.split()

        people.append(Person(person[0], person[1], Date(int(person[2]), int(person[3]), int(person[4]))))

month = int(input("zadajte mesiac pre vyhladanie: "))
day = input(f"zadajte den pre vyhladanie v mesiaci {month} (enter pre vyhladanie iba mesiaca): ")

people_to_show = []

for person in people:
    if person.birth_date.month == month and ((len(day) > 0 and person.birth_date.day == int(day)) or len(day) == 0):
        people_to_show.append(person)

if len(people_to_show) > 0:
    if len(day) > 0:
        print(f"NARODENINY DNA {day}.{month}:")

        for person in people_to_show:
            print(f"{person}: {2025 - person.birth_date.year} rokov")
    else:
        print(f"NARODENINY V MESIACI {month}:")

        for person in people_to_show:
            print(f"{person}: {person.birth_date}")
