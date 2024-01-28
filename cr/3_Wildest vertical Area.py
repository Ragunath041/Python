class Solution:
    def wildverticalarea(self,lst: list[list[int]]) -> int:
        lst_a = [x for x , y in lst]
        lst_a.sort()
        res = 0
        for i in range(1 , len(lst_a)):
            x = lst_a[i] - lst_a[i - 1]
            res = max(res , x)
        return res    

n = int(input())
lst = []
for i in range(n):
    a = list(map(int,input().split()))
    lst.append(a)

# lst = [[8,7],[9,9],[7,4],[9,7]]
sol = Solution()
ans = sol.wildverticalarea(lst)

print(ans)