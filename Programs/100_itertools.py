from itertools import count
x , y = 500 , 100 
c = count(x , y)
for i in c:
    print(i)
    if i == 1000:
        break

