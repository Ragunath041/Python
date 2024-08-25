from itertools import permutations
# n = int(input())
# a = list(map(str , input().split()))
# b = list(map(str , input().split()))
n = 4
a = ['12','56','908','234']
b = ['432','65','890','21']
sol = []
for x in range(n):
    for j in range(n):
        lst = []
        for i in  [i for i in list(permutations(b[j]))]:
            lst.append("".join(i))
        # print(lst)
        if a[x] in lst:
            pairs = ''
            pairs += str(x)
            pairs += str(j)
            sol.append(",".join(pairs))

print(*sol)