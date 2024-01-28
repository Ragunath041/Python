from collections import Counter
class Solution:
    def arithmeticTriplets(self, nums, diff) -> int:
        count = 0
        num_count = Counter(nums)  
        for num in nums:
            if num - diff in num_count and num + diff in num_count:
                count += 1   
        return count
solution_obj = Solution()
input_nums = [0,1,4,6,7,10]
difference = 3
result = solution_obj.arithmeticTriplets(input_nums, difference)
print("Number of arithmetic triplets:", result)