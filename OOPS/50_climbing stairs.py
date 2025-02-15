class Solution:
    def climbing(self , n):
        if n <= 2:
            return n
        dp = [None] * (n + 1)
        dp[0] , dp[1] = 1 , 1
        for i in range(2 , n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
if __name__ == '__main__':
    obj = Solution()
    n = int(input())
    print(obj.climbing(n))