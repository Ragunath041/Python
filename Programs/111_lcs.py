def lcs(a , b , i , j):
    if i < 0 or j < 0:
        return 0
    if a[i - 1] == b[j - 1]:
        return 1 + lcs(a , b , i - 1 , j - 1)
    c = lcs(a , b , i , j - 1)
    d = lcs(a , b , i - 1 , j)
    return max(a , b) 

str_1 = input()
str_2 = input()
ans = lcs(str_1 , str_2 , len(str_1), len(str_2))
print(ans)