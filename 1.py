from collections import defaultdict

def print_odd_occurrences(arr):
    # Create a defaultdict to store the count of each element
    counts = defaultdict(int)
    
    
    # Count occurrences of each element
    for num in arr:
        counts[num] += 1
    print(counts)
    
    # Print elements with odd counts
    for num, count in counts.items():
        if count % 2 != 0:
            print(num)

# Example usage
arr = [2 , 2 , 3 , 1 , 1]
print_odd_occurrences(arr)
