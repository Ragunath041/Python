import sys
def minCoins(coins , n , summ):
    if summ==0:
        return 0
    if summ < 0:
        return sys.maxsize
    res = summ
    for i in range(n):
        x = coins[i]
        res = min(res , minCoins(coins , n , summ - x) + 1)
    return res
summ = int(input())
coins = list(map(int,input().split()))
n = len(coins)
ans = minCoins(coins , n , summ)
print(ans)