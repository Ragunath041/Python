arr = [12,23,34,45,56]
print(":-1 method :",arr[:-1])
arr = [arr[-1]] + arr[:-1]
print(*arr)