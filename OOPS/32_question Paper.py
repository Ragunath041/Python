# if __name__ == "__main__":
#     obj = Solution()
#     x = int(input())
#     s = int(input())
#     y = int(input())
#     m = int(input())
#     z = int(input())
#     c = int(input())
#     qst_pair = map(str,input().split())
#     q = input()



import math
def F(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans
def nCr(n, r):
    if n < 0 or r < 0:
        return 0
    return F(n) // (F(n-r) * F(r))
x = int(input())
e = int(input())
y = int(input())
m = int(input())
z = int(input())
h = int(input())
a, b, c = input().split()
ans = nCr(x, e) * nCr(y, m) * nCr(z, h)
print(ans)
mx = 0
my = 0
mz = 0
XXX = ord(a) - ord('A') + 1
if XXX <= x:
    mx += 1
elif XXX <= x + y:
    my += 1
else:
    mz += 1
XXX = ord(b) - ord('A') + 1
if XXX <= x:
    mx += 1
elif XXX <= x + y:
    my += 1
else:
    mz += 1
ans -= nCr(x - mx, e - mx) * nCr(y - my, m - my) * nCr(z - mz, h - mz)
XXX = ord(c) - ord('A') + 1
if XXX <= x:
    mx += 1
    ans -= nCr(x - 1, e - 1) * nCr(y, m) * nCr(z, h)
elif XXX <= x + y:
    my += 1
    ans -= nCr(x, e) * nCr(y - 1, m - 1) * nCr(z, h)
else:
    mz += 1
    ans -= nCr(x, e) * nCr(y, m) * nCr(z - 1, h - 1)
ans = ans + 1 + nCr(x - mx, e - mx) * nCr(y - my, m - my) * nCr(z - mz, h - mz)
print(ans)