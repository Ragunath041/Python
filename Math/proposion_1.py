# 3   x
# - = -
# 6   4

a1,a2,b1,b2 = map(int,input().split())

if a2 == 0:
    x = b2 * a1 / b1
    print(x)
elif b2 == 0:
    y = b1 * a2 / b2
    print(y)
