def helper(a , b):
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                count += 1
    return count
a1 = [2,3,2]
a2 = [1,2]
x = helper(a1 , a2)
y = helper(a2 , a1)
print(x , y)