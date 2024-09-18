from collections import defaultdict
def helper(s , e , mapp):
    mapp[s] = 1
    for i in graph[s]:
        if not mapp[i]:
            helper(i , e , mapp)
mapp = {}
for _ in range(int(input())):
    n = int(input())
    mapp[n] = 0
graph = defaultdict(list)
for _ in range(int(input())):
    a , b = map(int,input().split())
    graph[a].append(b)
src = int(input())
end = int(input())
helper(src , end , mapp)
print(mapp[end])