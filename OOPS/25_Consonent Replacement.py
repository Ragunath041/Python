s = input()
ans = ''
for i in range(len(s)):
    a = s[i]
    aci = ord(a)
    print(aci , end=' ')
    a_prev = chr(aci - 1)
    a_next = chr(aci + 1)
    if a in ['A' , 'E' , 'I' , 'O' , 'U']:
        ans += a
    elif a_prev in  ['A' , 'E' , 'I' , 'O' , 'U']:
        ans += a_next
    else:
        ans += a_prev
print()
print(ans)
