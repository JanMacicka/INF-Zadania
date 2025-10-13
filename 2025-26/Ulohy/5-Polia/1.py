import random

def min(array: list[int]) -> int:
    min = array[0]
    index = 0

    for i, element in enumerate(array):
        if element < min:
            min = element
            index = i

    return min, index

def max(array: list[int]) -> int:
    max = array[0]
    index = 0

    for i, element in enumerate(array):
        if element > max:
            max = element
            index = i

    return max, index

def sum(array: list[int]) -> int:
    sum = 0

    for element in array:
        sum += element

    return sum

def clear(array: list[int], index: int) -> list[int]:
    return array[:index] + array[index + 1:]

def reverse(array: list[int]) -> list[int]:
    return array[::-1]

def rotate(array: list[int], diff: int) -> list[int]:
    return array[- diff:] + array[:- diff]


array = []

for i in range(random.randint(5, 10)):
    array.append(random.randint(0, 10))

print(array)

array_min = min(array)[0]
array_max = max(array)[0]

print(f"minimum: {array_min}, maximum: {array_max}")

min_pos = min(array)[1]
array[min_pos] = array[0]
array[0] = array_min

max_pos = max(array)[1]
array[max_pos] = array[-1]
array[-1] = array_max

print(f"priemer: {sum(array) / len(array)}")

array_2 = array

array_2.remove(array_max)

max_2 = max(array_2)

print(f"maximum 2: {max_2[0]}, {max_2[1]}. pozicia")

minims = []
maxims = []

for index, element in enumerate(array):
    if element == array_min:
        minims.append((index, element))

    if element == array_max:
        maxims.append((index, element))

print(f"minima (pozicia, hodnota): {minims}, maxima (pozicia, hodnota): {maxims}")

array.append(random.randint(0, 10))

print(f"rotacia o 1 dolava: {rotate(array, 1)}, rotacia o 1 doprava: {rotate(array, - 1)}")

n = int(input("zadajte svoju rotaciu: "))

print(f"rotacia o vase n: {rotate(array, n)}")