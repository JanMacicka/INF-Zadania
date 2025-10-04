x = int(input("zadajte prejdenu vzdialenost za 1. den: "))
y = int(input("zadajte ocakavany pocet km: "))

days = 1

while x < y:
    x *= 1.1
    days += 1

print(f"vzdialenost {round(x, 2)} prejdete na {days}. den")