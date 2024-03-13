class Solution:
    def nthcar(self,s,r,n):
        lst = [i for i in str(s)]
        ss = ''
        while r != 0:
            for i in range(len(lst)):
                if lst[i] == '1':
                    ss += '10'
                elif lst[i] == '0':
                    ss += '01'
                # if len(ss) > 0:
                #     break
            s = ss
            r -= 1
        return s[n]

obj = Solution()
# s = int(input())
# r = int(input())
# n = int(input())

s = 1011
r = 2
n = 3
ans = obj.nthcar(s,r,n)
print(ans)