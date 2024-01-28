def fact(f):
    if f == 0:
        return 1
    else:
        return f * fact(f - 1)

def digit_split(n,l):
    lst = []
    while n > 0:
        dig = n % 10
        lst.append(fact(dig))
        n //= 10
    return lst[::-1]

num = int(input())
size = len(str(num))
digit = digit_split(num,size) 
ans = sum(digit)
if num == ans:
    print("It's an Strong Number")
else:
    print("It's Not an Strong Number")