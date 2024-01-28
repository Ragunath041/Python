def max_subarray_sum(arr):
    max_sum = float('-inf')  # Initialize with negative infinity
    current_sum = 0

    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Number of test cases
t = int(input("Enter the number of test cases: "))

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = max_subarray_sum(arr)
    print(result)
