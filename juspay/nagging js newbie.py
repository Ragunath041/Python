from collections import defaultdict
import heapq
graph = defaultdict(list)
mapp = {}
for i in range(int(input())):
    n = int(input())
    mapp[n] = float('inf')
for i in range(int(input())):
    a , b , time = map(int,input().split())
    graph[a].append([b , time])
src = int(input())
end = int(input())
pq = []
mapp[src] = 0
heapq.heappush(pq , (0 , src))
while pq:
    curr_dis , u = heapq.heappop(pq)
    for v , weight in graph[u]:
        if mapp[v] > mapp[u] + weight:
            mapp[v] = mapp[u] + weight
            heapq.heappush(pq , (mapp[v] , v))

if mapp[end] == float('inf'):
    print(-1)
else:
    print(mapp[end])
