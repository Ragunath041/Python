row , col = map(int,input().split())
arr = []
for i in range(row):
    lst = list(map(int,input().split()))
    arr.append(lst)
target = int(input())
ans = ""
for i in range(row):
    for j in range(col):
        if arr[i][j] == target:
            ans += str(i)
            ans += str(j)
            break
    break
x = ",".join(ans)
print(f"({x})" if x else "-1 -1")