class Solution:
    def function(self , height):
        n = len(height)
        l , r = 0 , n - 1
        left_bar , right_bar = 0 , 0
        ans = 0

        while l <= r:
            if height[l] <= height[r]:
                if left_bar <= height[l]:
                    left_bar = height[l]
                else:
                    ans += left_bar - height[l]
                l += 1
            else:
                if right_bar <= height[r]:
                    right_bar = height[r]
                else:
                    ans += right_bar - height[r]
                r -= 1
        return ans
if __name__ == '__main__':
    obj = Solution()
    lst = list(map(int,input().split()))
    print(obj.function(lst))