class Solution:
    def function(self , n):
        if n <= 1:
            return 1
        dp = [0] * (n + 2)
        dp[1] = 1
        for i in range(2 , n + 2):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n + 1]

if __name__ == '__main__':
    obj = Solution()
    n = int(input())
    print(obj.function(n))