def digit_frequency(n):
    for i in range(9):
        if i in n:
            return 1
        else:
            return 0


num = int(input())
ans = digit_frequency(num)
print(f,"{} : {}")