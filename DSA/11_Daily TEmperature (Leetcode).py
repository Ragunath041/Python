class Solution:
    def dailyTemperature(self,temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []

        for i , j in enumerate(temperatures):
            while stack and j > stack[-1][0]:
                tem , ind = stack.pop()
                res[ind] = (i - ind)
            stack.append([j,i])
        return res



lst = list(map(int,input("Temperatures : ").split()))
obj = Solution()
answer = obj.dailyTemperature(lst)
print(answer)