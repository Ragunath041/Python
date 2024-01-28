from typing import List
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def countSetBits(n):
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count
        ans = 0
        for i, num in enumerate(nums):
            set_bits_count = countSetBits(i)
            if set_bits_count == k:
                ans += num
        return ans
nums_list = [3, 2, 5, 7, 8]
k_value = 2
sol = Solution()
result = sol.sumIndicesWithKSetBits(nums_list, k_value)
print("Sum of indices with", k_value, "set bits in their binary representation:", result)
