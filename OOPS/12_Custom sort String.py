from collections import Counter
class Solution:
    def customerSortingString(self,order,s):
        count = Counter(s)
        arr = []
        for i in order:
            if i in count:
                arr.extend([i] * count[i])

                del count[i]
        for i , j in count.items():
            arr.extend([i] * j)
        return ''.join(arr)  


obj = Solution()
order = 'kqep'
s = 'pekeq'
ans = obj.customerSortingString(order,s)
print(ans)
