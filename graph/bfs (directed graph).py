from collections import deque
def bfs(V , adj):
    queue = deque()
    visited = [0] * (V + 1)
    queue.append(0)
    visited[0] = 0
    while queue:
        # ans = []
        node = queue.popleft()
        # ans.append(node)
        print(node , end = " ")
        for nei in adj[node]:
            if not visited[nei]:
                queue.append(nei)
                visited[nei] = 1
    # return ans



n , e = map(int,input().split())
adj = [[] for _ in range(n + 1)]
for i in range(e):
    x , y = map(int,input().split())
    adj[x].append(y)
# print(bfs(n,adj))
bfs(n , adj)