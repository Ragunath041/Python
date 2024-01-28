class Solution:
    def mergeSortedArray(self, nums1: list[int], nums2: list[int]) -> list[int]:
        j = 0
        for i in range(len(nums1)):
            if nums1[i] == 0 and j < len(nums2):
                nums1[i] = nums2[j]
                j += 1
        return sorted(nums1)

nums1 = list(map(int, input("Enter elements for nums1: ").split()))
nums2 = list(map(int, input("Enter elements for nums2: ").split()))

a = Solution()
ans = a.mergeSortedArray(nums1, nums2)
print(ans)
