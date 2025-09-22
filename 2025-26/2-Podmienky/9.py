weight = float(input("zadajte hmotnost [kg]: "))
height = float(input("zadajte vysku [m]: "))

bmi = weight / height ** 2

if bmi < 18.5:
    print("podvaha")
elif bmi >= 18.5 and bmi < 25:
    print("normalna hmotnost")
elif bmi >= 25 and bmi < 30:
    print("biana")
elif bmi >= 30:
    print("steiner")