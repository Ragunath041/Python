import sys
def mcp(n , m , mat , r , c):
    if r == 0 or c == 0:
        return mat[0][0]
    elif r == -1 or c == -1:
        return sys.maxsize
    else:
        return min(mcp(n , m , mat , r-1 , c ) , mcp(n ,m, mat , r , c-1)) + mat[r][c]
n = int(input())
m = int(input())
mat = []
for i in range(n):
    temp = list(map(int,input().split()))
    mat.append(temp)
ans = mcp(n , m , mat , n - 1 ,  m - 1)
print(ans)











# def mcp(n, m, mat, r, c):
#     if r == 0 or c == 0:
#         return mat[0][0]
#     elif r == -1 or c == -1:
#         return float("inf")
#     else:
#         return min(mcp(n, m, mat, r-1, c) , mcp(n, m, mat, r, c-1)) + mat[r][c]

# n = int(input())
# m = int(input())
# mat = []
# for i in range(n):
#     temp = list(map(int, input().split()))
#     mat.append(temp)
# ans = mcp(n, m, mat, n - 1, m - 1)
# print(ans)
