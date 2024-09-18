from collections import defaultdict
lst = [-1, 0, 0, 1, 1, 2, 2]
child =defaultdict(list)
for i in range(len(lst)):
    if lst[i] != -1:
        child[lst[i]].append(i)
print(child)