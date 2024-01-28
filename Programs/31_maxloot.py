def max_count(n, lst):
    a = 0
    for i in range(n):
        for j in range(n):
            total = lst[i][j]  
            if i - 1 >= 0:
                total += lst[i - 1][j] 
            if i + 1 < n:
                total += lst[i + 1][j]  
            if j - 1 >= 0:
                total += lst[i][j - 1]  
            if j + 1 < n:
                total += lst[i][j + 1]  
            if i - 1 >= 0 and j - 1 >= 0:
                total += lst[i - 1][j - 1]  
            if i - 1 >= 0 and j + 1 < n:
                total += lst[i - 1][j + 1] 
            if i + 1 < n and j - 1 >= 0:
                total += lst[i + 1][j - 1]
            if i + 1 < n and j + 1 < n:
                total += lst[i + 1][j + 1]  
            a = max(a, total)
    return a
n = int(input())
lst = []
for x in range(n):
    row = list(map(int, input().split()))
    lst.append(row)
ans = max_count(n, lst)
print(ans)