def ans(n):
    if n <= 1:
        return 1
    return ans(n - 1) + ans(n - 2)
n = int(input())
print(ans(n))