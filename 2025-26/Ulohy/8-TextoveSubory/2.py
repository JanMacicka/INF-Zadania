text = ""

with open("2.txt", "r") as f:
    text = f.read().strip()

freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for entry in freq:
    print(f"{entry}: {freq[entry]}")
