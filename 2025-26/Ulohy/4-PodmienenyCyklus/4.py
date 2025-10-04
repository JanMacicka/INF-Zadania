def is_prime(number):
    if number <= 1:
        return False
    
    number_division = number - 1
    while number_division > 1:
        if number % number_division == 0:
            return False
        
        number_division -= 1
        
    return True

num = int(input("zadajte cislo: "))

print(is_prime(num))