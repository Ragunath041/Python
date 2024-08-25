V , E = map(int,input().split())
adj = [[]for _ in range(V)]
for _ in range(E):
    x , y = map(int,input().split())
    adj[x - 1].append(y)
    adj[y - 1].append(x)
# for _ in adj:
#     print(_)
for _ in range(1 , len(adj) + 1):
    if adj:
        print(f"{_} -> {len(adj[_ - 1])}")