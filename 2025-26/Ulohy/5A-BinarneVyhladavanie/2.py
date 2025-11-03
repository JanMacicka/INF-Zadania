def binary_search(array: list[int], low: int, high: int, x: int) -> int:
    if high >= low:
        mid = (low + high) // 2

        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search(array, low, mid - 1, x)
        else:
            return binary_search(array, mid + 1, high, x)
    else:
        return None
    

array = [1, 3, 3, 3, 5, 8, 8, 10]
element = int(input("zadajte prvok na zistenie pocetnosti v zozname: "))
original_occurence = binary_search(array, 0, len(array) - 1, element)
count = 1

occurence = original_occurence - 1

while occurence > 0:
    if not array[occurence] == element:
        break

    occurence -= 1
    count += 1

occurence = original_occurence + 1

while occurence < len(array):
    if not array[occurence] == element:
        break

    occurence += 1
    count += 1

print(f"cislo {element} sa nachadza {count}-krat")
