N = 100
num = 1

while num < N:
    num_to_sum = num
    divisible = True

    while num_to_sum > 0:
        digit = num_to_sum % 10
        num_to_sum = num_to_sum // 10

        if digit == 0 or num % digit != 0:
            divisible = False
            break
    
    if divisible: print(num)

    num += 1