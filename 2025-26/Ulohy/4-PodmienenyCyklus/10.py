num = int(input())

power_sum = 0
num_to_sum = num

while num_to_sum > 0:
    digit = num_to_sum % 10
    num_to_sum = num_to_sum // 10

    power_sum += digit ** 3

if num == power_sum:
    print("je armstrongovo cislo")
else:
    print("nie je armstrongovo cislo")