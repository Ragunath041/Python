import sys

# n = int(input("Enter the Number : "))
# ans = [i for i in range(n)]
# print(f"{sum(ans)}- The Size Required For performing is {sys.getsizeof(ans)}")
# ans = (i for i in range(n))
# print(f"{sum(ans)} - The Size Required For performing is {sys.getsizeof(ans)}")

def length(arr):
    count = 0
    for _ in arr:
        count += 1
    return count 
lst = [i for i in range(1 , 10)]
a = len(lst)
b = length(lst)
print(sys.getsizeof(a))
print(sys.getsizeof(b))