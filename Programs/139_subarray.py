lst = list(map(int,input().split()))
arr = []
for i in range(len(lst)):
    for j in range(i , len(lst)):
        arr.append(lst[i : j + 1])
print(arr)