arr = [5,3,2,1,4]
first = arr[0]
for i in range(len(arr)):
    if arr[i] > first:
        first = arr[i]
print(first)