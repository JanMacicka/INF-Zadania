class Measurement:
    def __init__(self, id: str, date: str, time: str, temp: float, clouds: str) -> None:
        self.id = id
        self.date = date
        self.time = time
        self.temp = temp
        self.clouds = clouds
        date_values = date.split(".")
        self.day = date_values[2]
        self.month = date_values[1]
        self.year = date_values[0]


    def __str__(self) -> str:
        return f"{self.day}/{self.month}/{self.year}"


def main() -> None:
    measurements = []

    with open("Pisomka-1-Pocasie.txt", "r") as f:
        for row in f.readlines():
            values = row.split()
            measurements.append(Measurement(values[0], values[1], values[2], float(values[3]), values[4]))

    print(f"celkovy pocet merani: {len(measurements)}")
    print(f"namerane teploty: {', '.join(str(x.temp) for x in sorted(measurements, key=lambda m: m.temp))}")
    print("dni, kedy bolo jasno:")

    for measurement in measurements:
        if measurement.clouds == "JJ":
            print(measurement)

    
if __name__ == "__main__":
    main()
