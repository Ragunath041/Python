class Solution:
    def answer(self, lst):
        row , col , p = len(lst) , len(lst[0]) , 0
        for i in range(row):
            for j in range(col):
                if lst[i][j] == 1:
                    p += 4
                    if lst[i - 1][j] == 1 and i > 0:
                        p -= 2
                    if lst[i][j - 1] == 1 and j > 0:
                        p -= 2
        return p
                
if __name__ == '__main__':
    obj = Solution()
    n = int(input())
    lst = []
    for _ in range(n):
        arr = list(map(int,input().split()))
        lst.append(arr)
    #lst = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(obj.answer(lst))
