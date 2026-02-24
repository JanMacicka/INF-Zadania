import random


def is_palindrome(num: str) -> bool:
    return num == num[::-1]


def main() -> None:
    amount = int(input("zadajte pocet cisel: "))
    numbers = [str(j) for j in [random.randint(0, 1000) for i in range(amount)]]
    palindromes = []

    for number in numbers:
        if is_palindrome(number):
            palindromes.append(number)
            print("\033[91m" + number + "\033[0m")
        else:
            print(number)

    coef = int(input("zadajte koeficient palindromu: "))

    with open("2-Palindromy.txt", "w") as f:
        for palindrome in palindromes:
            if len(palindrome) == 3 and int(palindrome[-2]) < coef:
                f.write(f"{palindrome}\n")


if __name__ == "__main__":
    main()
