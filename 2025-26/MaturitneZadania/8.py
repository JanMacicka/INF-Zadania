class Trip:
    def __init__(self, date: str, dist: float, duration: int, destination: str) -> None:
        self.date = date
        self.day = int(self.date[4:])
        self.month = int(self.date[2:4])
        self.year = 2000 + int(self.date[:2])
        self.dist = dist
        self.duration = f"{duration // 60}:{duration % 60:02d}"
        self.avg_speed = round(self.dist / (duration / 60), 1)
        self.destination = destination


    def __str__(self) -> str:
        return f"{self.date} {self.dist} {self.duration} {self.avg_speed} {self.destination}"


def main() -> None:
    trips = []

    with open("8-Cyklovylety.txt", "r") as f:
        for row in f.readlines():
            trip = row.split()
            
            trips.append(Trip(trip[0], float(trip[1]), int(trip[2]), " ".join(trip[3:])))

    month = int(input("zadajte mesiac na vyhladanie: "))
    month_trips = []

    for trip in trips:
        if trip.month == month:
            month_trips.append(trip)

    print(f"celkovy pocet vyletov v mesiaci {month}: {len(month_trips)}")
    print("\n".join([str(trip) for trip in month_trips]))


if __name__ == "__main__":
    main()
