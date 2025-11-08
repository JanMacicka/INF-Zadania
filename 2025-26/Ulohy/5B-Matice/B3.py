def pyramids(amount: int, rows_count: int) -> None:
    for i in range(1, rows_count + 1):
        print((" " * (rows_count - i) + "* " * i + " " * (rows_count - i + 1)) * amount)


pyramids(3, 5)
