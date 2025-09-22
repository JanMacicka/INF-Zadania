day = int(input("zadajte den narodenia: "))
month = int(input("zadajte mesiac narodenia: "))

match month:
    case 1:
        if day < 21:
            print("kozorozec")
        else:
            print("vodnar")
    case 2:
        if day < 20:
            print("vodnar")
        else:
            print("ryby")
    case 3:
        if day < 21:
            print("ryby")
        else:
            print("baran")
    case 4:
        if day < 21:
            print("baran")
        else:
            print("byk")
    case 5:
        if day < 21:
            print("byk")
        else:
            print("blizenci")
    case 6:
        if day < 22:
            print("blizenci")
        else:
            print("rak")
    case 7:
        if day < 23:
            print("rak")
        else:
            print("lev")
    case 8:
        if day < 24:
            print("lev")
        else:
            print("panna")
    case 9:
        if day < 24:
            print("panna")
        else:
            print("vahy")
    case 10:
        if day < 24:
            print("vahy")
        else:
            print("skorpion")
    case 11:
        if day < 23:
            print("skorpion")
        else:
            print("strelec")
    case 12:
        if day < 22:
            print("strelec")
        else:
            print("kozorozec")