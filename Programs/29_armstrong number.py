def armstrong(start, end):
    lst = []
    
    for i in range(start, end + 1):
        length = len(str(i))
        sum = 0
        temp = i
        
        while temp > 0:
            digit = temp % 10
            sum += digit ** length
            temp //= 10
        
        if i == sum:
            lst.append(i)
    
    return lst

m = int(input())
n = int(input())

arm = armstrong(m, n)

if len(arm) == 0:
    print(0)
else:
    ans = '\n'.join(map(str, arm))
    print(ans)
