# n = int(input())
# bridge = list(map(str,input().split()))
# groom = list(map(str,input().split()))
n = 4
bridge = ['r' , 'r' , 'm' , 'm']
groom = ['m' , 'r' , 'm' , 'r']
# r r m m 
# m r m r
x = "X"
c = 0
for i in range(n):
    for j in range(n):
        if bridge[i] == groom[j]:
            bridge[i] = x
            groom[j] = x
            break
    if bridge[i] != x:
        break
for i in range(n):
    if bridge[i] != x:
        c += 1
print(c)
print(bridge)
print(groom)