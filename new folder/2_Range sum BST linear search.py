arr = [10 , 5 , 15 , 3 , 7 , 13 , 18 , 1 , None , 6]
summ = 0
l = 6
h = 10
for i in arr:
    if i == None:
        continue
    if i in range(l , h + 1):
        summ += i
print(summ)