class Game:
    def __compress_steps(self, steps: str) -> str:
        new_steps = ""
        last_step = ""

        for i, step in enumerate(steps):
            if last_step == step:
                continue

            last_step = step
            occurences = 1

            for j in range(i + 1, len(steps)):
                if step != steps[j]:
                    break

                occurences += 1

            new_steps += f"{step} {occurences} "

        return new_steps


    def __init__(self, steps: str) -> None:
        self.steps = steps
        self.length = len(self.steps)
        self.compressed_steps = self.__compress_steps(self.steps)


def main() -> None:
    games = []
    
    with open("11-Hada.txt", "r") as f:
        for row in f.readlines():
            games.append(Game(row.strip()))

    print(f"pocet hier: {len(games)}")

    longest_game = None

    for game in games:
        if longest_game is None or game.length > longest_game.length:
            longest_game = game

    print(f"najdlhsia hra mala {longest_game.length} krokov")

    with open("11-Hada-Skomprimovany.txt", "w") as f:
        for game in games:
            f.write(f"{game.compressed_steps}\n")


if __name__ == "__main__":
    main()
