def rotation(matrix):
    n = len(matrix)
    m = len(matrix[0])
    arr = [[0] * n for _ in range(m)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            arr[j][m - 1 - i] = matrix[i][j]
    return arr

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(rotation(matrix))
print(m_diagonal(matrix))
print(s_diagonal(matrix))
# q = [0,1,2]
# for i in q:
#     if i == 0:
#         rotation(matrix)
#     if i == 1:
#         m_diagonal(matrix)
#     if i == 2:
#         s_diagonal(matrix)