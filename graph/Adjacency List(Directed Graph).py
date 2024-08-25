V , E = map(int,input("Node and Edges : ").split())
adj_list = []
for _ in range(V + 1):
    adj_list.append([])
for _ in range(E):
    x , y = map(int,input().split())
    adj_list[x].append(y)
for _ in range(len(adj_list)):
    if adj_list[i]:
        print(f"{_} : {sorted(adj_list[_])}")