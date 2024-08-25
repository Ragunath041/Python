lst = []
n = int(input("Enter the range of element : "))
for i in range(n):
    x = int(input())
    lst.append(x)
a , b , c = float('-inf') , float('-inf') , float('-inf')
for i in lst:
    if i > a:
        c = b
        b = a
        a = i
    elif i > b and i < a:
        c = b 
        b = i
    elif a > c and a > b:
        c = i
print(f"The Third Maximum Element is : {c}")