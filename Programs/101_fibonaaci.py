n = int(input())
f , s = 0 , 1
arr = []
for i in range(2 , n + 1):
    f , s = s , f + s
    arr.append(s)
print(arr[n - 1])