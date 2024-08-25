def fib(n):
    dp = [0 , 1]
    if n <= 1:
        return n
    for i in range(2 , n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]
    
n = int(input())
print(fib(n))