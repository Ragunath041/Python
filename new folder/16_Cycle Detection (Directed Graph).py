from collections import defaultdict
def is_cyclic(graph , n):
    visited = [0] * n
    path_Visited = [0] * n

    def dfs(n):
        visited[n] = path_Visited[n] = 1
        for i in graph[n]:
            if not visited[i]:
                if dfs(i):
                    return True
            elif path_Visited[i]:
                return True
        path_Visited[n] = 0
        return False

    for start in range(n):
        if not visited[start]:
            if dfs(start):
                return True
    return False
n , e = map(int,input().split())
graph = defaultdict(list)
for _ in range(e):
    x , y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
if is_cyclic(graph , n):
    print("Yes")
else:
    print("No")