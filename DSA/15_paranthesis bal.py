from collections import deque

stack = deque()
s = '[()]{}{[()()}'

for i in s:
    if i in ('(', '[', '{'):
        stack.append(i)
    else:
        if stack and ((stack[-1] == '(' and i == ')') or (stack[-1] == '[' and i == ']') or (stack[-1] == '{' and i == '}')):
            stack.pop()
        else:
            print("False")
            break

if len(stack) == 0:
    print("True")
else:
    print("False")
