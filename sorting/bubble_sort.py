lst = [6,5,3,1,8,7,2,4]
for i in range(len(lst)):
    for j in range(i):
        if int(lst[j]) > int(lst[j+1]):
            lst[j],lst[j+1] = lst[j+1],lst[j]
print(lst)