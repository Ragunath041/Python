def fib(n , a , b):
    while n > 0:
        x = a
        a = b + a
        b = x
        n -= 1
    return x
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_nums_range(n1, n2):
    prime_nums = []
    for i in range(n1, n2 + 1):
        if is_prime(i):
            prime_nums.append(i)
    return prime_nums

n1, n2 = map(int,input().split())
arr = prime_nums_range(n1 , n2)
print(arr)
c = []
for i in range(len(arr)):
    for j in range(i , len(arr)):
        c.append(str(arr[i]) + str(arr[j]))
# print(c)
p = []
for i in range(len(c)):
    if is_prime(int(c[i])):
        p.append(c[i])
# print(p)
z = []
for _ in p:
    z.append(int(_))
# print(z)
length = len(z)
f1 = min(z)
f2 = max(z)
# print(f1 , f2)
ans = fib(length - 2 , f1 , f2)
print(ans)