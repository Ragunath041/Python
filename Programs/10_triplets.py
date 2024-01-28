# Python3 program to find a triplet sum in array 
# that sum to a given value
  
def findTriplet(arr, n, target):
  
    # Fix the first element as arr[i]
    for i in range( 0, n-2):
  
        # Fix the second element as arr[j]
        for j in range(i + 1, n-1): 
              
            # Now find the third number
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    print("Triplet is", arr[i],
                          ", ", arr[j], ", ",arr[k])
                    return True
      
    # triplet not found
    return False
  
# Driver program to test above function 
arr = [1,3,4,5];
target = 5;
n = len(arr)
findTriplet(arr, n, target)
  
