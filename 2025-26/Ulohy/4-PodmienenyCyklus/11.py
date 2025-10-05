

num = 1000

while num < 10000:
    num_to_sum = num
    sum_1 = 0

    sum_1 = num_to_sum % 100
    num_to_sum = num_to_sum // 100    

    if (sum_1 + num_to_sum) ** 2 == num:
        print(num)

    num += 1