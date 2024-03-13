class Solution:
    def getCommon(self, nums1, nums2):
        ans = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ans.append(nums1[i])
            else:
                continue
        return min(ans)

a = Solution()
nums1 = [1,2,3,6]
nums2 = [2,3,4,5]
ans = a.getCommon(nums1 , nums2)
print(ans)