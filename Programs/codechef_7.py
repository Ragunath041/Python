# lst = list(s)
# r  = len(s) - 1
# l = 0
# while l <= r:
#     lst[l] , lst[r] = lst[r] , lst[l]
#     l += 1
#     r -= 1
# print(''.join(lst))

s = 'Ragunath'
l = len(s) - 1
i = 0
while i < l:
    i += 1
    if i ==  l:
        print(''.join(s[i])) 
l -= 1
i = 0

#print(s[l])

#for i in s:    