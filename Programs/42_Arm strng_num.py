def digit_split(n,l):
    lst = []
    while n > 0:
        digit = n % 10
        lst.append(digit ** l)
        n = n // 10
    return lst[::-1] 

num = int(input("Enter the number :"))
size = len(str(num))
digit_Split = digit_split(num,size)
ans = sum(digit_Split)

if num == ans:
    print("It's a Armstrong Number!")
else:
    print("It's Not an Armstrong number!")
