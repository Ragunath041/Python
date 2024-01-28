class Solution:
    def makingFilenameUniqu(self,lst : list[str]) -> list[str]:
        k = 0
        hashing = {}
        sol_list = []
        games = ''
        for i in lst:
            if i not in hashing:
                i.append(sol_list)
            else:
                k += 1
                games = i + '({k})'
                hashing += games
        return sol_list


lst = list(map(str,input().split()))
a = Solution()
ans = a.makingFilenameUniqu(lst)
print(ans)