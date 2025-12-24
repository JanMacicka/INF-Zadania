import random
def binary_search(array: list[float], low: int, high: int, x: float) -> int:
    """
    rekurzivna implementacia binarneho vyhladavania

    vracia index najdeneho prvku, ak existuje
    """
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


days = int(input("zadajte pocet dni: "))
# vygeneruje ceny
prices = [round(random.randint(150, 190) / 100, 2) for _ in range(days)]

# vypise vygenerovane ceny
print("ceny:")
print(", ".join(str(price) for price in prices))

# inicializujeme premenne na vypocet min a max
min, max = (prices[0], 0), (prices[0], 0)

for index, price in enumerate(prices):
    if price < min[0]:
        min = price, index

    if price > max[0]:
        max = price, index

print(f"najnizsia suma: {min[0]} €, {min[1] + 1}. pozicia")
print(f"najvyssia suma: {max[0]} €, {max[1] + 1}. pozicia")

# inicializujeme premenne na vypocet priemeru
price_sum = 0

for price in prices:
    price_sum += price

average = round(price_sum / days, 2)

print(f"priemerna cena: {average} €")

# presunieme hodnoty vzhladom na priemer (upravena implementacia bubble sortu)
for i in range(days):
    for j in range(i + 1, days):
        if prices[j] < average:
            prices[i], prices[j] = prices[j], prices[i]      

print("ceny vzhladom na priemer:")
print(", ".join(str(price) for price in prices))

# utriedime pole
prices = sorted(prices)
element = float(input("zadajte sumu na vyhladanie [€]: "))
result = binary_search(prices, 0, days - 1, element)

if result != None:
    print(f"suma {element} sa tu nachadza")
else:
    print(f"suma {element} sa tu nenachadza")

print(prices)
