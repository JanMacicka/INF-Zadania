array = [12, "x", None, 3.14, range(5), "123"]

for element in array:
    if type(element) == int or type(element) == float:
        print(f"{element} - cislo")
    elif type(element) == str:
        print(f"{element} - retazec")
    else:
        print(f"{element} - iny typ")
