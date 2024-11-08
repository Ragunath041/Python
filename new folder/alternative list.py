def merge(arr , left , right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return
    mid = n // 2
    left = []
    right = []
    for i in range(mid):
        left.append(arr[i])
    for j in range(mid , n):
        right.append(arr[j])
    merge_sort(left)
    merge_sort(right)
    merge(arr , left , right)

lst = list(map(int,input().split()))
merge_sort(lst)
n = len(lst)
ans = []
i , j = 0 , n - 1
while i <= j:
    ans.append(lst[j])
    if i != j:
        ans.append(lst[i])
    i += 1
    j -= 1
print(ans)