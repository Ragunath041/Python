class Solution:
    def maxArea(self,arr):
        result = []
        left , right = 0 , len(arr) - 1

        while left < right:
            area = (right - left) * min(arr[left] , arr[right])
            result.append(area)

            if arr[left] < arr[right]:
                left = left + 1
            else:
                right = right - 1
        return max(result)
obj = Solution()
arr = list(map(int,input().split()))
ans = obj.maxArea(arr)
print(ans)