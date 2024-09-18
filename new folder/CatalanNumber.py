def fact(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2 , n + 1):
        dp[i] = i * dp[i - 1]
    return dp[n]
def CatalanNumber(n):
    a = fact(2 * n)
    b = fact(n + 1)
    c = fact(n)
    return a // (b * c)
n = int(input())
if n == 0:
    print(0)
else:
    print(CatalanNumber(n))