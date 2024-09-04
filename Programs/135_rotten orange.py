from collections import deque
def rotten(grid):
    row = len(grid)
    col = len(grid[0])
    q = deque()
    f_or = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                q.append((i , j , 0))
            if grid[i][j] == 1:
                f_or += 1
    row_dir , col_dir = [1 , 0 , -1 , 0] , [0 , -1 , 0 , 1]
    max_time , c= 0 , 0
    run = 0
    while q:
        i,j,t=q.popleft()
        max_time=max(max_time,t)
        for k in range(4):
            nr=i+row_dir[k]
            nc=j+col_dir[k]
            if(nr>=0 and nr<row and nc>=0 and nc<col and grid[nr][nc]==1):
                grid[nr][nc]=2
                q.append((nr,nc,t+1))
                c+=1
    return max_time if c == f_or else -1
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(rotten(grid))





# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         n=len(grid)
#         m=len(grid[0])
#         q=deque()
#         f=0
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j]==2:
#                     q.append((i,j,0))
#                 elif grid[i][j]==1:
#                     f+=1
#         dr=[1,0,-1,0]
#         dc=[0,-1,0,1]
#         mt=0
#         c=0
        # while q:
        #     i,j,t=q.popleft()
        #     mt=max(mt,t)
        #     for k in range(4):
        #         nr=i+dr[k]
        #         nc=j+dc[k]
        #         if(nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc]==1):
        #             grid[nr][nc]=2
        #             q.append((nr,nc,t+1))
        #             c+=1
#         if c==f:
#             return mt
#         else:
#             return -1