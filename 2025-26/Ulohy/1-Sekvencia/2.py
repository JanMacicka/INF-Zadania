from math import pi

podiel = 223 / 71
zlomky = 22 / 17 + 37 / 47 + 88 / 83
mocnina = 99 / (2206 * 2 ** (1/2))
odmocnina = ((5 ** (1/2) + 6) ** (1/2) + 7) ** (1/2)
desat = (10 ** 100 / 11222.11122) ** (1/193)

hodnoty = [podiel, zlomky, mocnina, odmocnina, desat]

for hodnota in hodnoty:
    print(abs(pi - hodnota))