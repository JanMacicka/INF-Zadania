import math

def binary_square_root(number: float, low: float, high: float, accuracy: float) -> float:
    if high < low:
        return None
    
    mid = (low + high) / 2
    square = mid ** 2

    if abs(square - number) <= accuracy:
        return mid
    
    if square < number:
        return binary_square_root(number, mid, high, accuracy)
    else:
        return binary_square_root(number, low, mid, accuracy)
        

number = int(input("zadajte cislo na odmocnenie: "))
accuracy = float(input("zadajte presnost: "))
result = binary_square_root(number, 1, number, accuracy)

print(f"odmocnina z {number} je priblizne {round(result, abs(int(round(math.log10(accuracy)))))}")
