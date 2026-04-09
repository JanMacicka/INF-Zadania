def main() -> None:
    chars = ["{:x}".format(x) for x in range(0, 16)]
    text = ""
    codes = []
    base = 0

    with open("22-Text-Kod.txt", "r") as f:
        text = f.readline().lower()
    
    for i, char in enumerate(chars[::-1]):
            if char in text:
                base = len(chars) - i

                break

    codes = [text[i: i + 8] for i in range(0, len(text), 8)]

    if base >= 2:
        print("".join([chr(int(code, base)) for code in codes]))


if __name__ == "__main__":
    main()
