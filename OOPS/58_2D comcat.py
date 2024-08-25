arr = [['a','b','c'] , ['e','f','g','h'] , ['i','j' , 'k' ,'l'] , ['m','n','o','p']]   #"['aeg','afg'.....'cfj']"
res = []
l = len(arr)
#print(l)
for i in range(l):
    for j in range(l+1):
        res.append(arr[i][j])
        res.append(arr[i][j + 1])
print(res)

