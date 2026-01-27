class Stock:
    def __init__(self, id: str, amount: int, price: float) -> None:
        self.id = id
        self.amount = amount
        self.price = price

    
    def __str__(self) -> str:
        return self.id


def main() -> None:
    stock = []

    with open("3-KodTovaru.txt", "r") as f:
        for row in f.readlines():
            values = row.split()

            stock.append(Stock(values[0], int(values[1]), float(values[2])))

    stock = sorted(stock, key=lambda x: x.price)
    total = 0
    least: Stock = None

    for obj in stock:
        total += obj.price * obj.amount

        if least is None or least.amount >= obj.amount:
            least = obj

    print(f"pocet druhov tovaru: {len(stock)}")
    print(f"celkova hodnota tovaru: {round(total, 2)}")
    print(f"tovar s najmensim poctom kusov: {least}")
    print("prvych 5 najlacnejsich tovarov:")

    for i in range(5):
        if len(stock) < i + 1:
            break

        print(f"{stock[i]}: {stock[i].price}")


if __name__ == "__main__":
    main()
