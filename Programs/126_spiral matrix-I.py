# [
#     [1,2,3]
#     [4,5,6]
#     [7,8,9]
# ]

m , n = map(int,input().split())
matirx = []
for _ in range(m):
    arr = list(map(int,input().split()))
    matirx.append(arr)
top , bottom = 0 , m - 1
left , right = 0 , n - 1
ans = []
while top <= bottom and left <= right:
    for i in range(left , right + 1):
        ans.append(matirx[top][i])
    top += 1
    for i in range(top , bottom + 1):
        ans.append(matirx[i][bottom])
    right -= 1

    if top <= bottom:
        for i in range(right , left - 1 , -1):
            ans.append(matirx[bottom][i])
        bottom -= 1
    if left <= right:
        for i in range(bottom , top - 1 , -1):
            ans.append(matirx[i][left])
        left += 1
print(ans)