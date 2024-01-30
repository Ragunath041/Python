from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        a = Counter(nums)
        b = dict(a)

        max_count = max(b.values())
        maj_element = [i for i , j in b.items() if j == max_count][0]
        return maj_element

arr = list(map(int,input("Enter the List : ").split()))
a = Solution()
answer = a.majorityElement(arr)
print(f'Majority Element is {answer}')