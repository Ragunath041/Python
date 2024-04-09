class Solution:
    def lamp_toggler(self , n):
        l = ['F'] * n
        r = 1
        while r <= n:
            for i in range(r , n):
                if l[i - 1] == "F":
                    l[i - 1] = "O"
                else:
                    l[i - 1] = "F" 
            r += 1 
        return l.count('O')
if __name__ == "__main__":
    obj = Solution()
    n = int(input() )
    ans = obj.lamp_toggler(n)
    print(ans)