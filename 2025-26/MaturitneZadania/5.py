def main() -> None:
    keys = []
    text = ""
    encrypted_text = ""
    
    with open("5-Text.txt", "r") as f:
        rows = f.readlines()
        keys = [int(x) for x in rows[0].strip().split()][:-1]
        text = rows[1].strip()

    print(f"kluce: {", ".join(str(x) for x in keys)}")
    print(f"nezasifrovany text: {text}")

    for i, char in enumerate(text):
        if char == " ":
            encrypted_text += " "

            continue

        new_code = ord(char) + keys[i % (len(keys))]

        if new_code > 122:
            new_code -= 26

        encrypted_text += chr(new_code) 

    value = input("stlacte \"1\" pre vypisanie zasifrovaneho textu do konzoly (inak sa text zapise do suboru): ")

    if value == "1":
        print([encrypted_text])
    else:
        with open("5-ZasifrovanyText.txt", "w") as f:
            f.write(encrypted_text)


if __name__ == "__main__":
    main()
