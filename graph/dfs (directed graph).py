n , e = map(int,input().split())
adj = [[] for _ in range(n + 1)]
for i in range(e):
    x , y = map(int,input().split())
    adj[x].append(y)
for _ in adj:
    print(_)