def is_prime(n):
    if n == 2:
        return True
    if n <= 1:
        return False
    if n % 2 == 0:
        return False
    a = int(n ** 0.5) + 1
    for i in range(3 , a , 2):
        if n % i == 0:
            return False
    return True

n = int(input("Enter the Number :"))
print(is_prime(n))