def nested_sqrt(n: int) -> float:
    if n == 1:
        return 2 ** (1 / 2)
    else:
        return (2 + nested_sqrt(n - 1)) ** (1 / 2)
