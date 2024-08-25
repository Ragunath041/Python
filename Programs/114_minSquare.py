import math
def minsquare(n):
    if n <= 3:
        return n
    if(math.sqrt(n) == math.floor(math.sqrt(n))):
        return 1
    res = n
    for i in range(n):
        res = min(res , minsquare(n - 1) + 1)
    return res
n = int(input())
print(minsquare(n))


