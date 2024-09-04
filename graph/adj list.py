from collections import defaultdict
n , e = map(int,input().split())
graph = defaultdict(list)
for i in range(e):
    x , y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
print(dict(graph))