E = int(input())
adj = []
for _ in range(E):
    arr = list(map(int,input().split()))
    adj.append(arr)
matrix = [[adj[j][i] for j in range(len(adj))] for i in range(len(adj[0]))]
if matrix == adj:
    print("Its Undirected Graph")
else:
    print("Its Directed Graph")