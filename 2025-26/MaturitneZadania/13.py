import random


def deparse_guesses(string: str) -> list[int]:
    return [int(x) for x in string.split()]


def check_guesses(nums_guess: list[int], nums: list[int]) -> list[int]:
    correct = []
    
    for guess in nums_guess:
        if guess in nums:
            correct.append(guess)

    return correct


def main() -> None:
    nums_guess = deparse_guesses(input("zadajte 6 cisel oddelenych medzerou: "))
    nums = random.sample(range(1, 50), 6)
    correct_guesses = check_guesses(nums_guess, nums)
    correct_guess_count = len(correct_guesses)

    print("vyzrebovane cisla:")
    print(", ".join(str(x) for x in nums))
    print(f"pocet spravnych tipov: {correct_guess_count}")

    if correct_guess_count > 0:
        print(f"spravne tipy: {", ".join(str(x) for x in correct_guesses)}")


    user_guesses = []
    correct_user_guesses_counts = {x: 0 for x in range(1, 7)}

    with open("13-Loteria-2.txt", "r") as f:
        for row in f.readlines():
            user_guesses.append(deparse_guesses(row))

    for guesses in user_guesses:
        correct = len(check_guesses(guesses, nums))

        if correct > 0:
            correct_user_guesses_counts[correct] += 1

    for correct_guess_count in correct_user_guesses_counts.keys():
        print(f"{correct_guess_count} spravnych tipov malo {correct_user_guesses_counts[correct_guess_count]} ludi")


if __name__ == "__main__":
    main()
