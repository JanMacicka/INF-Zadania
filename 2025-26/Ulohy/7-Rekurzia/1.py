def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    
    return x * power(x, n - 1)
