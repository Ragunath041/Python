
# formula : a1/b1 = a2/b2

a1,a2,b1,b2 = map(int,input().split())

x = a1 * b2
y = b1 * a2

if x == y :
    print(x)
else:
    print(y)