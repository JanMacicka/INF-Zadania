def rotated_binary_search(array: list[int], low: int, high: int, x: int) -> int:
    if low > high:
        return None
    
    mid = (low + high) // 2

    if array[mid] == x:
        return mid
    
    if array[low] <= array[mid]:
        if x >= array[low] and x < array[mid]:
            return rotated_binary_search(array, low, mid - 1, x)
        else:
            return rotated_binary_search(array, mid + 1, high, x)
    else:
        if x > array[mid] and x <= array[high]:
            return rotated_binary_search(array, mid + 1, high, x)
        else:
            return rotated_binary_search(array, low, mid - 1, x)
    

array = [15, 18, 2, 3, 6, 12]
element = int(input("zadajte prvok na vyhladanie v zozname: "))
result = rotated_binary_search(array, 0, len(array) - 1, element)

if result != None:
    print(f"prvok {element} sa nachadza na {result + 1}. pozicii")
else:
    print(f"prvok {element} sa tu nenachadza")
    