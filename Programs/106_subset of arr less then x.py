def fun(arr , sub_set , i , k , a):
    if i == n:
        for j in range(k):
            a[j] = sub_set[k]
    else:
        sub_set[k] = arr[i]
        fun(arr , sub_set , i + 1 , k + 1 , a)
        fun(arr , sub_set , i + 1 , k , a)
lst = list(map(int,input().split()))
n = len(lst)
arr = [0] * n
a = []
fun(lst , arr , 0 , 0 , a)
print(a)