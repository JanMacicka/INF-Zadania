def array_sum(array: list[int] = [0]) -> int:
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + array_sum(array[1:])
