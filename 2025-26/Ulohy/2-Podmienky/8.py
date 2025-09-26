spring = [4, 5, 6]
summer = [7, 8, 9]
autumn = [10, 11, 12]
winter = [1, 2, 3]

num = int(input("zadajte mesiac: "))

if num in spring:
    print("jar")
elif num in summer:
    print("leto")
elif num in autumn:
    print("jesen")
elif num in winter:
    print("zima")