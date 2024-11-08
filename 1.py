arr = [3,0 ,0,2,0,4]
res = 0
for i in range(len(arr)):
    left = arr[i]
    for l in range(i):
        left = max(left , arr[l])
    right = arr[i]
    for r in range(i):
        right = max(right , arr[r])
    res += min(left , right) - arr[i]
print(res)