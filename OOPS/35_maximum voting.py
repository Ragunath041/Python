from collections import Counter
class Solution:
    def helper(self, nums):
        count = Counter(nums)
        maxi = max(list(count.values()))
        names = []
        for i , j in count.items():
            if j == maxi:
                names.append(i)
        names.sort()
        print(names)
        return names[0] , maxi
if __name__ == "__main__":
    obj = Solution()
    lst = list(map(str,input().split()))
    ans = obj.helper(lst)
    print(*ans)