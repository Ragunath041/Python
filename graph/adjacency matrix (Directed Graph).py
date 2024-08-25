V , E = map(int,input("Enter No.of.Vertices and Edges : ").split())
adj = []
for _ in range(V + 1):
    adj.append([0] * (V + 1))
for i in range(E):
    x , y = map(int , input().split())
    adj[x][y] = 1
for arr in adj:
    print(arr)