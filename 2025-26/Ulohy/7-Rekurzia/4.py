def array_sum(array: list[int] = []) -> int:
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    else:
        return array[0] + array_sum(array[1:])
