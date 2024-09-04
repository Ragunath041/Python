from collections import defaultdict
def graph(n , prerequisites):
    visited = set()
    cycle = set()
    ans = []
    def dfs(i):
        if i in visited:
            return True
        if i in cycle:
            return False
        cycle.add(i)
        for j in adj[i]:
            if not dfs(j):
                return False
        cycle.remove(i)
        visited.add(i)
        ans.append(i)
        return True
    adj = defaultdict(list)
    for arr in prerequisites:
        x , y = arr
        adj[x].append(y)
    for _ in range(n):
        if _ not in adj:
            adj[_] = []
    for i_ in range(n):
        if not dfs(_):
            return []
    return ans
n = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(graph(n , prerequisites))