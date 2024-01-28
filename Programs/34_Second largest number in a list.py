def large(array):
    f_large = max(array)
    array.remove(f_large)
    s_large = max(array)
    return s_large
n = int(input())
arr = list(map(int, input().strip().split()))
ans = large(arr)
print(ans)
