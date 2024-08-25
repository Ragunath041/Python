from collections import defaultdict
E = int(input())
adj = []
for _ in range(E):
    arr = list(map(int,input().split()))
    adj.append(arr)
D = defaultdict(list)
for i in range(len(adj)):
    D[i + 1]
    for j in range(len(adj[i])):
        if adj[i][j] == 1:
            D[i].append(j)
print(dict(D))