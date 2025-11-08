def print_list(list: list[str]) -> None:
    print("   ".join(list))

def binary_search(array: list[tuple[str, str]], low: int, high: int, x: str) -> tuple[str, str]:
    if high >= low:
        mid = (low + high) // 2

        if array[mid][0][0] == x:
            return array[mid]
        elif ord(array[mid][0][0]) > ord(x):
            return binary_search(array, low, mid - 1, x)
        else:
            return binary_search(array, mid + 1, high, x)
    else:
        return None


boys = ["Roman", "Jozo", "Adam", "Michal", "Palo"]
girls = ["Monca", "Andrea", "Anka", "Lucia", "Petra"]
people = [(boys[i], girls[i]) for i in range(len(boys))]

print_list(boys)
print_list(girls)

n = len(people)

for i in range(n):
    for j in range(n - i - 1):
        if people[j][0] > people[j + 1][0]:
            people[j], people[j + 1] = people[j + 1], people[j]

print("chlapci: ", end="")

for person in people:
    print(person[0], end="   ")

print("\ndievcata: ", end="")

for person in people:
    print(person[1], end="   ")

length = 0

for person in people:
    length += len(person[0])

print(f"celkova dlzka retazcov v poli chlapci: {length}")

people_list = [f"{person[1]} + {person[0]}" for person in people]

print_list(people_list)

STARTING_LETTER = "P"

couple = binary_search(people, 0, len(people) - 1, STARTING_LETTER)

if not couple is None and couple[0][0] == couple[1][0]:
    print(f"par zacinajuci s danym pismenom existuje ({couple[1]} + {couple[0]})")
else:
    print("par zacinajuci s danym pismenom neexistuje")