import os
import random


def guess(word: str) -> None:
    current = "." * len(word)
    attempts = 10

    while attempts > 0:
        os.system("cls")
        print(f"ostavajuci pocet pokusov: {attempts}")
        print("uhadni slovo:")
        print(current)

        given_letter = input()[0]

        if given_letter in word:
            for i, letter in enumerate(word):
                if given_letter == letter:
                    current = current[:i] + letter + current[i + 1:]
        else:
            attempts -= 1

        if current == word:
            print(word)
            print("gratulujem, vyhral si!")
            return

    print(f"prehral si. hladane slovo bolo {word}.")


def main() -> None:
    words = []

    with open("15-Obesenec.txt", "r") as f:
        for row in f.readlines():
            words.append(row.strip())

    guess(random.choice(words))


if __name__ == "__main__":
    main()
