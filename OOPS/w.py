nums = [1,2,3,4]
arr = []
n = len(nums)
for i in range(n):
    for j in range(i , n):
        arr.append(nums[i : j + 1])
print(arr)