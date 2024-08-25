'''
INPUT: word = 'abcdefd' ch = 'd'
OUTPUT: 'dcbaefd
'''
from collections import deque
# word = input()
# ch = input()

word = 'abcdefd' 
ch = 'd'
stack = deque()
if ch not in word:
    print(word)
for i in word:
    if i != ch:
        stack.append(i)
    else:
        break
stack += ch
s = ''.join(i for i in stack)
l = len(s)
print(s[::-1] + word[l:])

    
