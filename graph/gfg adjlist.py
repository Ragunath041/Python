def printGraph(V , edges):
        adj = []
        for _ in range(V + 1):
            adj.append([])
        for i in range(len(edges)):
            x , y = edges[i]
            adj[x].append(y)
            adj[y].append(x)
            # print(list(edges[i]))
        print(adj)

V = 5
e = [[0,1],[0,4],[1,2],[1,3],[1,4],[2,3],[2,3],[3,4]]
printGraph(V , e)