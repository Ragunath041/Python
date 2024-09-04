from collections import defaultdict
class Graph:
    def __init__(self , node):
        self.node = node
        self.graph = defaultdict(list)
    def adding(self , x , y):
        self.graph[x].append(y)
        self.graph[y].append(x)
    def is_cycle(self):
        visited = [False] * (self.node + 1)
        def dfs(v , parent):
            visited[v] = True
            for i in self.graph[v]:
                if not visited[i]:
                    if dfs(i , v):
                        return True
                elif i != parent:
                    return True
            return False
        for i in range(1 , self.node + 1):
            if not visited[i]:
                if dfs(i , -1):
                    return True
        return False
n = int(input())
obj = Graph(n)
for _ in range(n - 1):
    x , y = map(int,input().split())
    obj.adding(x , y)
if obj.is_cycle():
    print("Its Cycle")
else:
    print("Not a Cycle")