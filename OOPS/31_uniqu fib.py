import math
from itertools import permutations
def fib(lst):
    if len(lst) < 2:
        return 0
    a , b = lst[0] , lst[-1]
    for _ in range(len(lst) - 2):
        a, b = b , a + b
    return b

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2 , int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def comp_num(a , b):
    prime_numbers = [i for i in range(a , b) if is_prime(i)]
    compositor = set()
    
    for x , y in permutations(prime_numbers , 2):
        compositor_num = int(str(x) + str(y))
        if is_prime(compositor_num):
            compositor.add(compositor_num)
    return sorted(compositor)


a , b = map(int,input().split())
comp = comp_num(a , b)
ans = fib(comp)
print(ans)