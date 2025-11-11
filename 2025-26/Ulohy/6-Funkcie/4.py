def divisors(n: int) -> list[int]:
    divisors = []

    for i in range(1, n ** 1 // 2):
        if n % i == 0 and not i in divisors:
            divisors.append(i)
            divisors.append(n // i)
    
    return sorted(divisors)

            
def divisor_sum(n: int) -> int:
    return sum(divisors(n))


def is_perfect(n: int) -> bool:
    return divisor_sum(n) - n == n


def all_perfect(start: int, end: int) -> list[int]:
    perfect = []

    for i in range(start, end + 1):
        if is_perfect(i):
            perfect.append(i)

    return perfect
