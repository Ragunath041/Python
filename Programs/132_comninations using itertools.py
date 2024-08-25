import itertools
arr = [1 , 2 , 3]
comb = []
for i in range(1 , len(arr) + 1):
    ele = [list(x) for x in itertools.combinations(arr , i)]
    comb.extend(ele)
print(comb)