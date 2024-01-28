class Solution:	
    def seriesSum(self,n):
        sum = (n*(n+1)) // 2
        return sum
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.seriesSum(n)
        print(ans)
        tc=tc-1
