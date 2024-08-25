def subSetOfArray(arr , sub_set , n , i , k , res , t):
    if i == n:
        if sum(sub_set[:k]) == t:
            res.append(sub_set[:k])
        return
     
    else:
        sub_set[k] = arr[i]
        subSetOfArray(arr , sub_set , n , i + 1 , k + 1 , res , t)
        subSetOfArray(arr , sub_set , n , i + 1 , k , res , t)
lst = list(map(int,input().split()))
n = len(lst)
sub_set = [0] * n
sub_arr = []
target = int(input())
subSetOfArray(lst ,sub_set ,  n , 0 , 0 , sub_arr , target)
print(sub_arr)
# if not sub_arr:
#     print("No")
# else:
#     print("YEs")  