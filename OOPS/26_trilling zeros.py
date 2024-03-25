class Solution:
    def trailing_zeros(self, num):
        s = str(num)
        l = len(s) - len(s.rstrip('0'))
        return l

if __name__ == '__main__':
    obj = Solution()
    # num = int(input("Enter a number: "))
    ans = obj.trailing_zeros(100220000)
    print(ans)
