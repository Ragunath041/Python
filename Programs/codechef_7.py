for i in range(int(input())):
    x , y = map(int,input().split())
    while x != 0:
        if x > y:
            temp = x
            x = y
            y = temp
        else:
            y = y - x
    print(y)