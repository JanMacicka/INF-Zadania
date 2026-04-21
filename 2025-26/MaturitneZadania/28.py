import random


def main() -> None:
    sentences = []
    shuffled_sentences = []

    with open("28-PoprehadzovanyText1-Vstup.txt", "r", encoding="ansi") as f:
        for row in f.readlines():
            sentences.append(row.strip())

    print(f"povodne vety:\n{'\n'.join(sentences)}")

    for sentence in sentences:
        shuffled_sentence = ""

        for word in sentence.split():
            shuffled_word = word[0] + "".join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1] if len(word) > 3 else word
            shuffled_sentence += shuffled_word + " "

        shuffled_sentences.append(shuffled_sentence)

    print(f"\nupravene vety:\n{'\n'.join(shuffled_sentences)}")

    with open("28-PoprehadzovanyText1-Vystup.txt", "w", encoding="ansi") as f:
        f.write("\n".join(shuffled_sentences))


if __name__ == "__main__":
    main()
