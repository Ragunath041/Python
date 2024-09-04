from collections import defaultdict
D = defaultdict(list)
arr = [[1,2],[2,3],[4,2]]
maxi = float("-inf")
for _ in arr:
    x , y = _
    D[x].append(y)
    D[y].append(x)
for key , value in D.items():
    if sum(value) > maxi:
        maxi = key
print(maxi)