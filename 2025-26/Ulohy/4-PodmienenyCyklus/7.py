num = 100
while num < 1000:
    num_sum = 0
    num_to_sum = num

    while num_to_sum > 0:
        num_sum += num_to_sum % 10
        num_to_sum = num_to_sum // 10

    if num_sum == 12:
        print(num)

    num += 1
    continue