def is_palindrome(number):
    original_num = number
    reversed_num = 0

    while original_num > 0:
        digit = original_num % 10
        reversed_num = reversed_num * 10 + digit
        original_num = original_num // 10

    return number == reversed_num

num = int(input("zadajte cislo: "))

while not is_palindrome(num):
    num += 1

print(f"najblizsi vacsi palindrom: {num}")
