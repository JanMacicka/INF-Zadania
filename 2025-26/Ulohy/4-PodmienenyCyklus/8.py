num = int(input())

num_sum = 0

while num > 0:
    digit = num % 10
    num = num // 10

    if digit % 2 != 0:
        num_sum += digit

print(num_sum)