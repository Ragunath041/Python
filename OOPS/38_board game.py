def minscore(a, n):
    ans = i = j = 0
    while i + 1 < n and j + 1 < n:
        if a[i + 1][j] < a[i][j + 1]:
            ans = (ans // 2) + a[i + 1][j]
            i = i + 1
        else:
            ans = (ans // 2) + a[i][j + 1]
            j = j + 1
    ans = (ans // 2) + a[n - 1][n - 1]
    return ans

if __name__ == "__main__":
    n = 5
    board = [[0, 82, 2, 6, 7],[4, 3, 1, 5, 21],[6, 4, 20, 2, 8],[6, 6, 64, 1, 8],[1, 65, 1, 6, 4]]
    print(minscore(board, n))