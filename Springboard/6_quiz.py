for i in 23, 45, 50, 65, 76, 90:
    if i % 5 != 0:
        continue
    if i % 10 == 0:
        print(i, end=" ")
        continue
    if i % 3 ==0:
        print(i,end =" ")