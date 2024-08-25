arr = list(map(int,input().split()))
n = len(arr)

for i in range(1 , n):
    temp = arr[i]
    j=i
    while j > 0 and arr[j - 1] > temp:
        arr[j] = arr[j - 1]
        j -= 1
    arr[j] = temp
print(*arr)

# arr.sort()
# print(arr)