import copy
def helper(graph):
    ans = [[] for _ in range(len(graph))]
    for i in range(len(graph)):
        ans[i].extend(graph[i])
    return ans

N , E = map(int,input().split())
graph = []
for _ in range(N + 1):
    graph.append([])
for _ in range(E):
    x , y = map(int,input().split())
    graph[x].append(y)
cloned_graph = helper(graph)
print(cloned_graph)