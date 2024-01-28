#   2     2
# 1 - + 3 - - 7 = ?
#   3     5


# Method - 1:

# print(1+2/3+3+2/5+(-7))

# Method - 2:

a1,a2,b1,b2,x,y,z = map(int,input().split())

x = (x + a1/b1 + y +  a2/b2 + z)

print(x)