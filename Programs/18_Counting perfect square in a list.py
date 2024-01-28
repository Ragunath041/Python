import math
n=int(input())
lst=[]
count=0
for i in range(n):
    temp=int(input())
    lst.append(temp)
for j in range(n):
    if math.isqrt(lst[j]) ** 2 == lst[j]:
        count+=1
print(count)