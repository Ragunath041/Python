class Binary:
    def binary(self,lst,n,k):
        low = 0
        high = n - 1
        while low <= high:
            mid = (high + low) // 2
            if lst[mid] == k:
                return mid
            elif lst[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        return -1
lst = []
n = int(input("Enter the Size of a list :"))
for i in range(n):
    temp = int(input())
    lst.append(temp)
k = int(input("Enter the finding Element :"))
obj = Binary()
ans = obj.binary(lst,n,k)
if ans != -1:
    print(f"The Element present in '{ans}' index")
else:
    print(f"'{k}' is not in the list")