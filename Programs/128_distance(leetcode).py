def maxDistance(arrays):
    if not arrays:
        return 0
    
    # Initialize with the first array
    min_value = arrays[0][0]
    max_value = arrays[0][-1]
    
    max_distance = 0
    
    # Iterate through the arrays starting from the second array
    for i in range(1, len(arrays)):
        current_min = arrays[i][0]
        current_max = arrays[i][-1]
        
        # Calculate potential maximum distances
        max_distance = max(max_distance, abs(current_max - min_value), abs(max_value - current_min))
        
        # Update the global min and max values
        min_value = min(min_value, current_min)
        max_value = max(max_value, current_max)
    
    return max_distance
        
arrays = [[1,2,3],[4,5],[1,2,3]]
print(maxDistance(arrays))  # Output: 4
