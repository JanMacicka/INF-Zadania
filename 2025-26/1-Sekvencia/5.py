num = int(input())

if num < 1000:
    exit

print(num // 10, num % 10)
print(num // 100, num % 100)
print(num // 1000, num % 1000)
print(num // 10000, num % 10000)