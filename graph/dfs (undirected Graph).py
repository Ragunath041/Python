def dfs(n):
    visited[n] = True
    print(n , end = ' ')
    for arr in adj[n]:
        if not visited[arr]:
            dfs(arr)


n , e = map(int,input().split())
adj = [[] for _ in range(n + 1)]
for i in range(e):
    x , y = map(int , input().split())
    adj[x].append(y)
    adj[y].append(x)
visited = [False] * (n + 1)

dfs(1)