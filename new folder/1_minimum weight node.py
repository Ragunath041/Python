def helper(arr):
    n = len(arr)
    weight = [0] * n
    max_weight = float('-inf')
    result = -1    
    for i in range(n):
        dest = arr[i]
        if dest != -1:
            weight[dest] +=i
    for i in range(n):
        if weight[i] >= max_weight:
            max_weight = weight[i]
            result = i
            
    print(result)

helper([1 ,2 ,1 ,1 ,2])