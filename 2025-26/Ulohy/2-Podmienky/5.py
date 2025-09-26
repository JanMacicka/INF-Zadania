def normal_to_f(x):
    return x * 1.8

def f_to_normal(x):
    return x / 1.8

values = ["c", "f", "k"]

temp = int(input("zadajte teplotu: "))
unit_from = input("zadajte jednotku [C, F, K]: ").lower()
unit_to = input("zadajte pozadovanu jednotku [C, F, K]: ").lower()

if unit_from not in values or unit_to not in values or unit_from == unit_to:
    print("ste jebnuty")
    exit

match unit_from:
    case  "c":
        match unit_to:
            case "f":
                print(normal_to_f(temp) + 32)
            case "k":
                print(temp + 273.15)

    case  "f":
        match unit_to:
            case "c":
                print(f_to_normal(temp - 32))
            case "k":
                print(f_to_normal(temp - 32) + 273.15)

    case  "k":
        match unit_to:
            case "c":
                print(temp - 273.15)
            case "f":
                print(normal_to_f(temp - 273.15) + 32)