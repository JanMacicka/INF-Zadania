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


array = [2, 5, 8, 12, 16, 23, 38, 56, 72]
element = int(input("zadajte prvok na vyhladanie v zozname: "))
result = binary_search(array, 0, len(array) - 1, element)

if result != None:
    print(f"prvok {element} sa nachadza na {result + 1}. pozicii")
else:
    print(f"prvok {element} sa tu nenachadza")