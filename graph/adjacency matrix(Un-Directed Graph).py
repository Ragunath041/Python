V , E = map(int , input("No.of.Vertices and Edges : ").split())
adj = []
for _ in range(V + 1):
    adj.append([0] * (V + 1))
for _ in range(E):
    x , y = map(int , input().split())
    adj[x][y] = 1
    adj[y][x] = 1
for _ in adj:
    print(_)
