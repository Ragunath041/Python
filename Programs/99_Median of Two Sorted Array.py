"""INPUT : 1)lst_1 = [1 , 3] , lst_2 = [2]    2) lst_1 = [1 , 2] , lst_2 = [3 , 4]
OUTPUT : 2) 2.00000 2) 2.50000"""

lst_1 = list(map(int,input().split()))
lst_2 = list(map(int,input().split()))
lst = sorted(lst_1 + lst_2)
l = len(lst)
x = l // 2
y = (l - 1) // 2
if x == y:
    print(format(lst[x] , '.5f'))
else:
    a = lst[x] + lst[y]
    print(format((a / 2) , '.5f'))