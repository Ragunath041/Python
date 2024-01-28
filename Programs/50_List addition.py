l1 = [2,4,3]
l2 = [5,6,4]
a,b=0,0
for i in l1:
    a = a*10+i
for j in l2:
    b = b*10+j
add = str(a + b) [::-1]
print([int(i) for i in add])