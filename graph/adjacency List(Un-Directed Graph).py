V , E = map(int , input("Vertices and Edges : ").split())
adj_list = [[]for _ in range(V + 1)]
for _ in range(E):
    x , y = map(int,input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)
for i in range(len(adj_list)):
    if adj_list[i]:
        print(f"{i} : {sorted(adj_list[i])}")

