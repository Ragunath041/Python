arr = list(map(int,input().split()))
k = int(input())
lst = []
for i in range(len(arr)):
    for j in range(i , len(arr)):
        if sum(arr[i : j + 1]) == k:
            lst.append(arr[i : j + 1])
print(lst)