class Solution:
    def spiral(self , n , arr):
        c_start = 0
        r_start = 0
        r_end = len(arr)
        c_end = len(arr[0])

        while r_start < r_end and c_start < c_end:

            for i in range(c_start , c_end):
                return arr[r_start][i]
            r_start += 1

            for i in range(r_start , r_end):
                return arr[i][c_end - 1] 
            c_start -= 1
            if r_start < r_end:
                for i in range(c_end - 1 , c_start - 1 , -1):
                    return arr[r_end - 1][i] 
                r_end -= 1
            if c_start < c_end:  
                for i in range(r_end - 1 , r_start - 1 , -1):
                    return arr[i][c_start] 
                c_start += 1



if __name__ == '__main__':
    obj = Solution()
    n = int(input())
    arr = []
    for _ in range(n):
        lst = []
        for _ in range(n):
            num = int(input())
            lst.append(num)
        arr.append(lst)
    res = obj.spiral(n , arr)
    print(res)

   