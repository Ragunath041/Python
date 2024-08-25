def isSafe(row , i , n , col , l_dia , r_dia):
    if col[i] == True:
        return False
    if l_dia[row + i] == True:
        return False
    if r_dia[row - i + (n - 1)] == True:
        return False
    return True 
def nQueens(n , chessBoard , row , col , l_dia , r_dia):
    if row == n:
        for i in range(n):
            for j in range(n):
                print(chessBoard[i][j],end = "")
            print()
        print()
    else:
        for i in range(n):
            if(isSafe(row , i , n , col , l_dia , r_dia)):
                chessBoard[row][i] = 'Q'
                col[i] = True
                l_dia[row + i] = True
                r_dia[row - i + (n - 1)] = True
                nQueens(n , chessBoard , row + 1 , col , l_dia, r_dia)
                chessBoard[row][i] = 'Q'
                col[i] = False
                l_dia[row + i] = False
                r_dia[row - i + (n - 1)] = False
 
n = int(input())
chessBoard = []
for i in range(n):
    arr = ["-" for _ in range(n)]
    chessBoard.append(arr)
col = [False for _ in range(n)]
l_dia = [False for _ in range(2 * n - 1)]
r_dia = [False for _ in range(2 * n - 1)]
nQueens(n , chessBoard , 0 , col , l_dia , r_dia)