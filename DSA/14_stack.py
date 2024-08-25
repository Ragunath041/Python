from collections import deque
stack = deque()
s = 'ABCDEF GHIJKL MNOPO QRST UVWXYZ'
ans = ''
for i in s:
    stack.append(i)
while stack:
    ans += stack.pop()
print(ans)


# s = 'ragunath'
# ans = ''
# for i in range(len(s) - 1 , -1 , -1):
#     ans += s[i]
# print(ans)
   