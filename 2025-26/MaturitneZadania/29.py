class Runner:
    def __init__(self, id: int, time: str, checkpoints: list[str]) -> None:
        self.id = id
        self.time = time
        self.checkpoints = checkpoints
        self.all_checkpoints = False

        minutes, seconds = time.split(":")
        self.seconds = int(minutes) * 60 + int(seconds)


    def __str__(self) -> str:
        return f"{self.id}\t{self.time}"


def main() -> None:
    checkpoints = []
    runners = []
    failed_runners = []

    with open("29-Stanovistia.txt", "r") as f:
        for row in f.readlines():
            checkpoints.append(row.strip())
    
    with open("29-Pretekari.txt", "r") as f:
        for row in f.readlines():
            values = row.split()
            current_checkpoints = []

            for checkpoint in values[2:]:
                if checkpoint in checkpoints:
                    current_checkpoints.append(checkpoint)
            
            runners.append(Runner(int(values[0]), values[1], current_checkpoints))

    runners = sorted(runners, key=lambda r: r.seconds)
    
    for runner in runners:
        if len(runner.checkpoints) == len(checkpoints) and runner.checkpoints[0] == checkpoints[0] and runner.checkpoints[-1] == checkpoints[-1]:
            runner.all_checkpoints = True
        else:
            runners.remove(runner)
            failed_runners.append(runner)

    print(f"vitaz: {runners[0].id}")
    print("vysledkova listina:")
    print("\n".join(str(r) for r in runners))
    print("nedokoncili:")
    print("\n".join(str(r) for r in failed_runners))

if __name__ == "__main__":
    main()
