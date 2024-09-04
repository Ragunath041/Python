from collections import defaultdict
arr = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
D = defaultdict(set)
source = 5
destination = 9
visited = set()
def dfs(n):
    if n == destination:
        return True
    visited.add(n)
    for i in D[n]:
        if i not in visited:
            if dfs(i):
                return True
    return False
for a , b in arr:
    D[a].add(b)
    D[b].add(a)
print(dfs(source))