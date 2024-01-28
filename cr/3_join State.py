for _ in range(int(input())):
    n , m = map(int,input().split())
    lst = list(map(int,input().split()))
    current_count , maximum_count  = 0 , 0
    
    for i in range(n):
        current_count += lst[i]
        
        if current_count >= m:
            maximum_count += 1
            current_count = 0
    print(maximum_count)