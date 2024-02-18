def is_prime(n):
    if n == 2:
        return True
    if n <= 1:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    divisior = int(n ** 0.5) + 1
    for i in range(3 , divisior , 2):
        if n % i == 0:
            return False
    return True

def prime_numbers(n):
    arr = []
    for i in range(2 , n + 1):
        if is_prime(i):
            arr.append(i)
    return arr

n = int(input('Enter the number :'))
print(prime_numbers(n))