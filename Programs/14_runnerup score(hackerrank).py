a=int(input())
lst=[]
for i in range(a):
    temp=int(input())
    x=lst.append(temp)
print(x)
b=list(set(lst))
srt=b.sort(reverse=True)
print(srt)
  
