n = int(input())
bridge = list(map(str,input().split()))
groom = list(map(str,input().split()))
x , c = "X" , 0
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
