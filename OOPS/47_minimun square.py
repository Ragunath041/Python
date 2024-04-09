def min_sqr(n):
    if n <= 3:
        return n
    res = n
    for i in range(1 , n + 1):
        temp = i * i
        if temp > n:
            break
        else:
            res = min(res , min_sqr(n - temp) + 1)
    return res
n = int(input())
print(min_sqr(n))