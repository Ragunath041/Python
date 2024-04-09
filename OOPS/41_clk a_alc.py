class Solution:
    def rotation(self, n):
        str_n = str(n)
        r = str_n[-1] + str_n[:-1]
        return int(r)
    def suffle(self, n , m):
        clk_w = [n]
        for i in range(3):
            n = self.rotation(n)
            clk_w.append(n)
        a = [m]
        for i in range(3):
            m = self.rotation(m)
            a.append(m)
            ans = a + clk_w
        return max(ans)

if __name__ == "__main__":
    obj = Solution()
    # n = int(input())
    n = 1234
    temp = str(n)[::-1]
    m = int(temp)
    ans = obj.suffle(n , m)
    print(ans)
