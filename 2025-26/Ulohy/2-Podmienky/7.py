height = int(input("zadajte vysku stetky [cm]: "))
dimensions = input("zadajte miery stetky [a-b-c]: ").split("-")

if dimensions == ["90", "60", "90"] and height >= 175:
    print("ideaal")
else:
    print("nem az a ideal stetka")