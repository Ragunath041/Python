from collections import defaultdict
def dfs(tree , s):
    for i in tree[s]:
        if i == end or len(tree[s]) == 0:
            return 
        else:
            ans.append(i)
            dfs(tree , i)
tree = defaultdict(list)
for i in range(int(input())):
    n = int(input())
    tree[n] = []
for i in range(int(input())):
    a , b = map(int,input().split())
    tree[a].append(b)
start = int(input())
end = int(input())
ans = [start]
dfs(tree , start)
ans.sort()
print(*ans)