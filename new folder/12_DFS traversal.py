from collections import defaultdict
class Graph:
    def __init__(self , node):
        self.node = node
        self.graph = defaultdict(list)
    def addingEdges(self , x , y):
        self.graph[x].append(y)
        self.graph[y].append(x)
    def dfsTraversal(self):
        visited = [False] * self.node
        ans = []
        def dfs(adj , s):
            visited[s] = True
            ans.append(s)
            for i in self.graph[s]:
                if not visited[i]:
                    dfs(self.graph , i)    
        dfs(self.graph , 0)
        return ans

    
n = int(input())
obj = Graph(n)
for _ in range(n - 1):
    x , y = map(int,input().split())
    obj.addingEdges(x , y)
print(obj.dfsTraversal())
    
