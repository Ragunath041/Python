from collections import Counter
class Solution:
    def frequency(self,arr):
        ans = []
        count = Counter(arr)
        sort = sorted(count.items() , key = lambda x : x[1])
        for i , j in sort:
            ans.extend([i] * j)
        return ans



if __name__ == "__main__":
    obj = Solution()
    arr = list(map(int,input().split()))
    res = obj.frequency(arr)
    print(res)
