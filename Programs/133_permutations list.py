def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        x = lst[i]
        rem = lst[:i] + lst[i + 1 :]
        for i in permutation(rem):
            l.append([x] + i)
    return l
arr = [1,2,3]
sol = []
for i in permutation(arr):
    sol.append(i)
for i in range(len(sol)):
    if sol[i] == arr:
        print(sol[i + 1])
