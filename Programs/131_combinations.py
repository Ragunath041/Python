import itertools
def combinations(arr):
    def helper(start , path):
        if path:
            res.append(path)
        for i in range(start , len(arr)):
            helper(i + 1, path + [arr[i]])
    res = []
    helper(0 , [])
    return res
arr = [1,4,2,5,3]
lst = combinations(arr)
res = 0
temp = []
# print(lst)
for z in range(len(lst)):
    if len(lst[z]) % 2 != 0:
        temp.append(lst[z])
        # res += sum(lst[z])
print(sum(temp[9]))
# for zz in range(len(temp)):
#     res += sum(temp[zz])
# print("sym : ",res)