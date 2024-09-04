from collections import defaultdict , deque
class Solution():
    def largestSumCycle(self, N, Edge):
        def is_cycle(adj):
            visited = set()
            parent = {}
            for start in graph:
                if start not in visited:
                    Q = deque([(start , None)])
                    visited.add(start)
                    while Q:
                        x , y = Q.popleft()
                        for j in graph[x]:
                            if j not in visited:
                                Q.append((j , x))
                                visited.add(j)
                                parent[j] = x
                            elif j != y:
                                return True
            return False
        D = defaultdict(list)
        largestSum_cycle = float("-inf")
        for _ in range(N):
            if Edge[_] != -1:
                D[_].append(Edge[_])
        graph = dict(D)
        if is_cycle(graph):
            def dfs(n):
                for i in graph[n]:
                    if i not in visit:
                        dfs(i)
                visit.add(n)
            visit = set()
            summ = 0
            for x , y in graph.items():
                for i in y:
                    if i not in visit:
                        dfs(i)
                    summ += i
                if summ > largestSum_cycle:
                    largestSum_cycle = max(largestSum_cycle , summ)
            return largestSum_cycle
        return -1
obj = Solution()
e = [1, 2, 0, -1]
print(obj.largestSumCycle(len(e) , e))