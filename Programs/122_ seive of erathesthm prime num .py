def is_prime(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p < n:
        if prime[p] == True:
            for i in range(p * p , n + 1 , p):
                prime[i] = False
        p += 1
    prime_nums = []
    for i in range(2 , n + 1):
        if prime[i] == True:
            prime_nums.append(i)
    # prime_nums = [i for i in range(2 , n + 1) if prime[i]]
    return prime_nums
n = int(input())
print(is_prime(n))