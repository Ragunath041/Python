def inf_stn(n, a):
    lst = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            top = a[i-1][j]
            bottom = a[i+1][j]
            left = a[i][j-1]
            right = a[i][j+1]
            if a[i][j] == top + bottom + left + right:
                lst.append(a[i][j])
    if len(lst) == 0:
        return -1
    else:
        return lst
n = int(input())
a = []
for x in range(n):
    row = list(map(int, input().split()))
    a.append(row)
result = inf_stn(n, a)
if result == -1:
    print(-1)
else:
    print(*result)
