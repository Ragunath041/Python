from collections import defaultdict
visited = set()
def dfs(i):
    if i in visited:
        return False
    if pre_req[i] == []:
        return True
    visited.add(i)
    for j in pre_req[i]:
        if not dfs(j):
            return False
    visited.remove(i)
    pre_req[i] = []
    return True
def main(n):
    ans = []
    for i in range(n):
        if not dfs(i):
            return False
    return True
n , e = map(int,input().split())
D = defaultdict(list)
for i in range(e):
    x , y = map(int,input().split())
    D[x].append(y)
for i in range(n):
    if i not in D:
        D[i] = []
pre_req = dict(sorted(D.items()))
print(main(n))