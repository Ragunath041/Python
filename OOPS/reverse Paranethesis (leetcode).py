from collections import deque
class Solution:
    def reverseParenthesis(self , s : str) -> str:
        stack = deque()
        for i in s:
            if i == '(':
                stack.append("(")
            elif i == ")":
                temp = []
                while stack and stack[-1] != "(":
                    temp.append(stack.pop()[::-1])
                stack.pop()
                stack.append("".join(temp))
            else:
                stack.append(i)
        return "".join(stack)

if __name__ == "__main__":
    obj = Solution()
    s = input()
    print(obj.reverseParenthesis(s))