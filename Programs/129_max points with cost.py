def maxpoint(points):
    n = len(points)
    index = []
    summ = 0
    for arr in points:
        m = max(arr)
        summ += m
        index.append(arr.index(m))
    x = 0
    for i in range(len(index) - 1):
        cost = abs(index[i] - index[i + 1])
        x += cost
    return summ - x


arr = [[1,5],[2,3],[4,2]]

print(maxpoint(arr))















# arr = [1,2,3,4,5,6]
# ans = 0
# for i in range(len(arr)-1):
#     x = abs(arr[i] - arr[i + 1])
#     ans += x
# print(ans)        