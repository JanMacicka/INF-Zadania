day = int(input("zadajte den narodenia: "))
month = int(input("zadajte mesiac narodenia: "))
year = int(input("zadajte rok narodenia: "))

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

if year % 12 == 0:
    print("cinsky horoskop: potkan")
elif year % 12 == 1:
    print("cinsky horoskop: byvol")
elif year % 12 == 2:
    print("cinsky horoskop: tiger")
elif year % 12 == 3:
    print("cinsky horoskop: zajac")
elif year % 12 == 4:
    print("cinsky horoskop: drak")
elif year % 12 == 5:
    print("cinsky horoskop: had")
elif year % 12 == 6:
    print("cinsky horoskop: kon")
elif year % 12 == 7:
    print("cinsky horoskop: ovca")
elif year % 12 == 8:
    print("cinsky horoskop: opica")
elif year % 12 == 9:
    print("cinsky horoskop: kohut")
elif year % 12 == 10:
    print("cinsky horoskop: pes")
elif year % 12 == 11:
    print("cinsky horoskop: kanec")
