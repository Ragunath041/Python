def orangesRotting(grid):
    def helper(i, j):
        flag = False
        if j < len(grid[0]) - 1 and grid[i][j] == 2:
            if grid[i][j + 1] == 1:
                grid[i][j + 1] = 2
                flag = True
        if i < len(grid) - 1 and grid[i][j] == 2:
            if grid[i + 1][j] == 1:
                grid[i + 1][j] = 2
                flag = True
        return flag
    count = 0 
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if helper(i, j):
                count += 1
    for row in grid:
        if 1 in row:  
            return -1  
    return count
grid = [[0,2]]
print(orangesRotting(grid))
