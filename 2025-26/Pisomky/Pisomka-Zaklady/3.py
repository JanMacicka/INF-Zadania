import os

choice = 0
original_number = 0

while not choice:
    os.system("cls")
    
    choice = int(input("z coho chcete konvertovat? [2 / 10]: "))

    if choice != 2 and choice != 10:
        print("ale no")
        continue

    original_number = input("zadajte cislo na prevod: ")

match choice:
    case 2:
        result = 0

        for i in range(len(original_number)):
            result += int(original_number[i]) * 2 ** (len(original_number) - i - 1)

        print(result)

    case 10:
        result = []
        number = int(original_number)
        
        while number > 0:
            result.append(number % 2)

            number = number // 2

        for i in range(len(result) - 1, -1, -1):
            print(result[i], end="")