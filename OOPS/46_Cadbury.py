def function(a , b):
    if a and b:
        return a // b + function(a%b , b) if a > b else b // a + function(a , b % a)
    return 0
p = int(input())
q = int(input())
r = int(input())
s = int(input())
t = 0
for i in range(p , q + 1):
    for j in range(r , s  + 1):
        t += function(i , j)
print(t)