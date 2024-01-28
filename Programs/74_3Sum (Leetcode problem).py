lst = list(map(int,input().split()))
ans = []
for i in range(len(lst)):
    for j in range(i + 1):
        for k in range(j + 1):
            if lst[i] + lst[j] + lst[k] == 0:
                ans.append(lst[i] + lst[j] + lst[k])
print(sorted(ans))


