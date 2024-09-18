def subset(arr , temp , n , i , k , lst):
    if i == n:
        for j in range(n):
            lst.append(temp[j]) 
    temp[k] = arr[i]
    subset(arr , temp[i] + arr[k] , n , i + 1 , k + 1 , lst)
    subset(arr , temp , n , i  , k + 1 , lst)

arr = list(map(int,input().split()))
# t = int(input())
temp = [0] * len(arr)
lst = []
subset(arr , temp , len(arr) , 0 ,0, lst)
print(lst)