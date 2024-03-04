class Sorted_sqr:
    def sorted_squrNum(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2        
        n = len(nums)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums
arr = list(map(int, input().split()))
obj = Sorted_sqr()
ans = obj.sorted_squrNum(arr)
print(ans)
