from collections import defaultdict
Edge = [-1]
ans = []
D = defaultdict(list)
for i in range(len(Edge)):
    if Edge[i] != -1:
        D[i].append(Edge[i])
in_degree = [[]for _ in range(len(Edge))]
for x, arr in D.items():
    for y in arr:
        in_degree[y].append(x)
for _ in in_degree:
    ans.append(sum(_))
maxi = float("-inf")
sol = 0
for i , j in enumerate(ans):
    if j > maxi:
        maxi = max(maxi , j)
for i , j in enumerate(ans):
    if j == maxi:
        ans = i
print(ans)
