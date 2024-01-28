prefix_sum = {}
current_sum = 0
N = 5
S = 12
A = [1, 2, 3, 7, 5]

for i, num in enumerate(A):
    current_sum += num
    if current_sum == S:
        print(1, i + 1)  # Adjust indices to be one-based
    if current_sum - S in prefix_sum:
        print(prefix_sum[current_sum - S] + 2, i + 1)  # Adjust indices to be one-based
    prefix_sum[current_sum] = i

print("No subarray found with the given sum")
