#using recurssion 

#def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)

#Using DP

#     if n == 0:
#         return 0
#     dp = [0] * (n + 1)
#     dp[1] = dp[2] = 1
#     for i in range(2 , n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
#     return dp[n]

#using memoization
def fib(n):
    memo = [1 , 1]
    if n == 0:
        return 0
    if n <= 2:
        return 1
    for i in range(2 , n    ):
        memo[i % 2] = memo[0] + memo[1]
    return memo[n % 2]






print(fib(5))