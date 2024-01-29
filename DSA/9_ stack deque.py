from collections import deque
stack = deque()

stack.append(10)
stack.append(30)
stack.append(23)
stack.append(22)
stack.append(1)
print(f'The List Items : {list(stack)}')

print(f'Pooped item => {stack.pop()}')

print(f'The remaining Items are {list(stack)}')