def reverse_fun(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10  # Update n by integer division
    return rev


# lst_1 = list(map(int, input().split()))
# lst_2 = list(map(int, input().split()))  

lst_1 = [2,4,3]
lst_2 = [5,6,4]
a = int("".join(map(str, lst_1)))  
b = int("".join(map(str, lst_2)))  

add = reverse_fun(a) + reverse_fun(b)
l = reverse_fun(add)
ans = [int(i) for i in str(l)]
print(ans)