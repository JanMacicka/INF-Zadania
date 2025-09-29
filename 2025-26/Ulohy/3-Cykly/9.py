num = int(input("zadajte cislicu (2 - 9): "))

if num < 2 or num > 9:
    print("ste kokot")
    exit()

for i in range(1, 101):
    num_string = str(i)
    sum = 0

    for value in num_string:
        sum += int(value)

    if str(num) in num_string or i % num == 0 or sum == num:
        print("*", end=" ")
    else:
        print(i, end=" ")
