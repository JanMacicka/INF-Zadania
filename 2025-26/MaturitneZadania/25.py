def main() -> None:
    groups = [" ", "ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"]
    cipher_table = {}
    used_fields = {str(x): 0 for x in range(9)}

    for i, group in enumerate(groups):
        for j, char in enumerate(group):
            cipher_table[char] = str(i) * (j + 1)

    text = input("zadajte zext na zasifrovanie: ")
    ciphered_text = ""

    for char in text:
        ciphered_text += cipher_table[char] + " "

    for char in ciphered_text:
        if char != " ":
            used_fields[char] += 1

    used_fields = {k: v for k, v in sorted(used_fields.items(), key=lambda item: item[1], reverse=True)}
    max_value = max(used_fields.values())
    most_frequent_codes = [k for k, v in used_fields.items() if v == max_value]

    print(f"zasifrovany text: {ciphered_text}")
    print(f"najcastejsie zvolene policka: {', '.join(most_frequent_codes)}")

if __name__ == "__main__":
    main()
