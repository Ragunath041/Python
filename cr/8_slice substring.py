def subarray_with_given_sum(arr, n, s):
    start = 0
    curr_sum = 0
    
    for end in range(n):
        curr_sum += arr[end]        
        while curr_sum > s and start < end:
            curr_sum -= arr[start]
            start += 1        
        if curr_sum == s:
            return [start + 1, end + 1]  
    return [-1]  
arr = [1, 2, 3, 4]
n = len(arr)
s = 0
print(subarray_with_given_sum(arr, n, s))  # Output: [2, 4]
