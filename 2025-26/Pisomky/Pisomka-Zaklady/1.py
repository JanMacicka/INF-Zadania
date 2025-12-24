def digit_sum(number):
    digit_sum = 0

    while number > 0:
        digit_sum += number % 10
        number = number // 10

    return digit_sum

num = int(input("zadajte cislo: "))

for i in range(1, num + 1):
    sum_current = digit_sum(i)

    if sum_current < digit_sum(num):
        print(f"{i} {sum_current}")