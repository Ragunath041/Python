def res(arr, r, l, i, k, M):
    global v
    if i == l:
        if k == M:
            min_val = min(r[:k])
            max_val = max(r[:k])
            if max_val - min_val < v:
                v = max_val - min_val
    else:
        r[k] = arr[i]
        res(arr, r, l, i + 1, k + 1, M)
        res(arr, r, l, i + 1, k, M)

N = int(input())
M = int(input())
arr = list(map(int,input().split()))
r = [0] * N
v = 99999
res(arr, r, N, 0, 0, M)
print(v)