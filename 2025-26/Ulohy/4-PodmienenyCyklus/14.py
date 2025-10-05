def is_palindrome(number):
    original_num = number
    reversed_num = 0

    while original_num > 0:
        digit = original_num % 10
        reversed_num = reversed_num * 10 + digit
        original_num = original_num // 10

    return number == reversed_num

num = int(input("zadajte cislo: "))

if is_palindrome(num):
    print("palindrom")
else:
    print("nie je palindrom")