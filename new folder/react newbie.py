def dfs(adj , s):
    for i in adj[s]:
        if i == end or len(adj[start]) == 0:
            return
        else:
            ans.append(i)
            dfs(adj , i)
D = {}
n = int(input())
for i in range(n):
    temp = int(input())
    D[temp] = []    
e = int(input())
for i in range(e):
    u , v = map(int , input().split())
    D[u].append(v)
start = int(input())
end = int(input())
ans = [start]
dfs(D , start)
ans.sort()
print(ans)
# for i in ans:
#     print(i , end = " ")