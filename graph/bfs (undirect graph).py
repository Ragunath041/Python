from collections import deque
def bfs(n , adj):
    queue = deque()
    visited = [0] * (n + 1)
    queue.append(0)
    visited[0] = 1
    arr = []
    while queue:
        node = queue.popleft()
        arr.append(node)
        for i in adj[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
    return arr
n , v = map(int,input().split())
adj = [[] for _ in range(n + 1)]
for i in range(v):
    x , y = map(int , input().split())
    adj[x].append(y)
    adj[y].append(x)
print(bfs(n , adj))