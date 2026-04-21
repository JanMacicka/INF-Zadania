def main() -> None:
    chars = {}
    encrypted_text = []
    freq_encrypted = {}
    decrypted_text = ""

    with open("30-Frekv.txt", "r") as f:
        for row in f.readlines():
            values = row.split()

            if row[0] != " ":
                chars[int(values[1])] = values[0]
            else:
                chars[int(values[0])] = " "

    with open("30-Sifro.txt", "r") as f:
        for row in f.readlines():
            encrypted_text.append(row.strip())

    for row in encrypted_text:
        for char in row:
            freq_encrypted[char] = 1 if not char in freq_encrypted.keys() else freq_encrypted[char] + 1

    for row in encrypted_text:
        decrypted_text += "\n"

        for char in row:
            decrypted_text += chars[freq_encrypted[char]]

    print(f"desifrovany text:{decrypted_text}")

    keys = ""

    for key in freq_encrypted.keys():
        keys += f"{key} -> {chars[freq_encrypted[key]]}\n"

    with open("30-Kluc.txt", "w") as f:
        f.write(keys)


if __name__ == "__main__":
    main()
