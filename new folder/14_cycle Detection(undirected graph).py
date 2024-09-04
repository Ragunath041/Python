from collections import deque , defaultdict
def is_cyclic(adj , V):
    visited = [0] * V

    def dfs(node , parent):
        visited[node] = 1
        for i in adj[node]:
            if not visited[i]:
                if dfs(i , node):
                    return True
            elif i != parent:
                return True
        return False

    for i in range(V):
        if not visited[i]:
            if dfs(i , -1):
                return True
    return False
n , e = map(int,input().split())
graph = defaultdict(list)
for i in range(e):
    x , y = map(int , input().split())
    graph[x].append(y)
    graph[y].append(x)
if is_cyclic(graph , n):
    print("Yes")
else:
    print("No")