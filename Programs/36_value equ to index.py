def indx_eql(lst,n):
    res = []
    for i in range(n):
        if lst[i] == i+1:
            res.append(lst[i])
    return res
lst = list(map(int,input().strip().split()))
n = len(lst)
ans = indx_eql(lst,n)
print(ans)