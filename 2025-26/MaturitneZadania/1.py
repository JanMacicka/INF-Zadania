HOPS = 10


class Ball:
    def __calculate_hops(self):
        hops = []

        for i in range(HOPS):
            hops.append((i + 1, round(self.height * self.coefficient ** i, 2)))

        return hops
    
    
    def __get_1_meter_hops(self) -> int:
        if self.hops[0][1] <= 1:
            return 0

        for hop in self.hops:
            if hop[1] <= 1:
                return hop[0] - 1
            
        return len(self.hops)
    

    def __init__(self, height: float, coefficient: float) -> None:
        self.height = height
        self.coefficient = coefficient
        self.hops = self.__calculate_hops()
        self.hops_1_meter = self.__get_1_meter_hops()


balls = []

with open("1-Lopticka.txt", "r") as f:
    for row in f.readlines():
        values = row.split()

        balls.append(Ball(float(values[0]), float(values[1])))

for ball in balls:
    print(f"pocet vyskoceni nad 1 meter: {ball.hops_1_meter}")

    for hop in ball.hops:
        print(f"{hop[0]}: {hop[1]} m") if hop[1] >= 1 else print(f"{hop[0]}: {round(hop[1] * 100)} cm")
