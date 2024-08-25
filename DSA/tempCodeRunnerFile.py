n = 9
#arr = list(input().split())
arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
ind_4 = arr.index('4')
ind_7 = arr.index('7')
print(ind_4 , ind_7)
lst = list(map(int , arr))
a = sum(lst[:ind_4])
print(a)
b = sum(lst[ind_7 + 1:])
print(b)
print(a + b)
