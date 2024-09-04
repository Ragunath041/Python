from collections import defaultdict , deque
class Solution():
    def largestSumCycle(self, N, Edge):
        def is_cycle(n , adj):
            visited = [0] * n
            parent = [0] * n
            def dfs(n):
                visited[n] = parent[n] = 1
                for i in adj[n]:
                    if not visited[i]:
                        if dfs(i):
                            return True
                    elif parent[i]:
                        return True
                parent[n] = 0
                return False
            for i in range(n):
                if not visited[i]:
                    if dfs(i):
                        return True
            return False
        D = defaultdict(list)
        largestSum_cycle = float("-inf")
        for _ in range(N):
            if Edge[_] != -1:
                D[_].append(Edge[_])
        graph = dict(D)
        if is_cycle(N , graph):
            return True
        else:
            return False
obj = Solution()
e = [0, 1, 2, 0, 2, 3, 4, 5, 6, 4, 5, 3, -1]
print(obj.largestSumCycle(len(e) , e))