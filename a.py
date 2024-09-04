class Solution:
    def numEnclaves(self , grid):
        count = 0
        n , m = len(grid) , len(grid[0])
        def helper(i , j):
            d_r = [0 , 1 , 0 , -1]
            d_c = [1 , 0 , -1 , 0]
            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                for k in range(4):
                    if grid[i][j] == 1 or grid[d_r[i]][d_c[i]] == 1:
                        grid[i][j] = 0
            return 1
        for i in range(n):
            for j in range(m):
                helper(i , j)
                count += 1
        print(grid)
        return count

obj = Solution()
grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print(obj.numEnclaves(grid))