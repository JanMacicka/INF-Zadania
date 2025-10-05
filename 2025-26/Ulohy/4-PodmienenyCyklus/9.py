num = int(input())

num_sum = 0
position = 1

while num > 0:
    digit = num % 10
    num = num // 10

    if position % 2 != 0:
        num_sum += digit

    position += 1

print(num_sum)