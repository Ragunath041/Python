class Solution:
    def numIslands(self , grid):
        row , col = len(grid) , len(grid[0])
        count = 0
        def helper(i , j):
            if i < 0 or i == row or j < 0 or j == col or grid[i][j] != '1':
                return 
            grid[i][j] = " "
            helper(i , j + 1)
            helper(i , j - 1)
            helper(i + 1 , j)
            helper(i - 1, j)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    helper(i , j)
                    count += 1
        print(grid)
        return count

obj = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(obj.numIslands(grid))