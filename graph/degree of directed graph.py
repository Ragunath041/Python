V , E = map(int,input().split())
out_degree = [[]for _ in range(V)]
in_degree = [[]for _ in range(V)]
for _ in range(E):
    x , y = map(int,input().split())
    out_degree[x - 1].append(y)
    in_degree[y - 1].append(x)
# for _ in adj:
#     print(_)
for _ in range(1 , E + 1):
    print(f"{_} -> In-Degree : {len(in_degree[_-1])} , Out-Degree : {len(out_degree[_ - 1])}")