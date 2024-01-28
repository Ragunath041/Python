# nums = list(map(int,input("Enter the List :").split()))
# n = int(input("Enter the number :"))
import itertools 
nums = [2, 5, 1, 3, 4, 7]
n = 3
a = [nums[n:]]
b = list(nums[:n])
ans = itertools.chain(*zip(b,a))
print(list(ans))
print(a)
print(b)