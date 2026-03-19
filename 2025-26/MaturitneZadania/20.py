class Stop:
    def __init__(self, embarked: int, disembarked: int, name: str) -> None:
        self.embarked = embarked
        self.disembarked = disembarked
        self.diff = embarked - disembarked
        self.name = name
        self.machine_needed = embarked >= 10
        self.request_stop = embarked < 3 and disembarked < 3


    def __str__(self) -> str:
        return self.name


def main():
    stops = []

    with open("20-DopravnyPrieskum.txt", "r", encoding="ansi") as f:
        for row in f.readlines():
            stop = row.strip().split(";")
            stops.append(Stop(int(stop[0]), int(stop[1]), stop[2]))

    current_passengers = 0
    max_passengers = current_passengers
    needed_machines = []
    request_stops = []
    
    print("pocty cestujucich:")
    
    for stop in stops:
        current_passengers += stop.diff
        vehicle = ""

        if current_passengers > max_passengers:
            max_passengers = current_passengers

        if max_passengers <= 10:
            vehicle = "kratka"
        elif max_passengers <= 25:
            vehicle = "standardna"
        else:
            vehicle = "dlha"

        if stop.machine_needed:
            needed_machines.append(stop)
        
        if stop.request_stop:
            request_stops.append(stop)

        print(f"{stop}: {current_passengers}")

    print(f"najvacsi pocet pasazierov: {max_passengers}, a preto treba typ elektricky {vehicle}")
    print("zastavky, kde je vhodne umiestnit automat: ", end="")
    print(", ".join([str(s) for s in needed_machines]))
    print("zastavky na znamenie: ", end="")
    print(", ".join([str(s) for s in request_stops]))


if __name__ == "__main__":
    main()
