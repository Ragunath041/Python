class Solution:
    def longest_rectangle_Histogram(self , heights):
        maximum = 0
        stack = []

        for i , j in enumerate(heights):
            start = i
            while stack and stack[-1][1] > j:
                index , height = stack.pop()
                maximum = max(maximum , height * (i - index))
                start = index
            stack.append((start , j))
        for i , j in stack:
            maximum = max(maximum , j * (len(heights) - i))
        return maximum

if __name__ == '__main__':
    obj = Solution()
    heights = list(map(int,input().split()))
    print(obj.longest_rectangle_Histogram(heights))