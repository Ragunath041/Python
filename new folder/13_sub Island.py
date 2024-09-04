class Solution:
    def countSubIslands(self, grid1 , grid2):
        row = len(grid2)  
        col = len(grid2[0])
        def dfs(i , j):
            if i < 0 or j < 0 or i >= row or j >= col or  grid2[i][j] == 0:
                return 
            if grid1[i][j] != 1:
                nonlocal flag 
                flag = False
            grid2[i][j] = 0
            dfs(i + 1 , j)
            dfs(i - 1 , j)
            dfs(i , j + 1)
            dfs(i , j - 1)
        count = 0
        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1:
                    flag = True
                    dfs(i , j)
                    if flag:
                        count += 1
        return count
obj = Solution()
grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
print(obj.countSubIslands(grid1 , grid2))
