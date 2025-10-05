num = int(input("zadajte cislo: "))

divisor = 1
divisor_sum = - num

while divisor <= num ** (1 / 2):
    if num % divisor == 0:
        divisor_sum += divisor
        divisor_sum += num // divisor

    if divisor_sum > num:
        print("nie je dokonale")
        exit()

    divisor += 1

if divisor_sum == num:
    print("je dokonale")
else:
    print("nie je dokonale")