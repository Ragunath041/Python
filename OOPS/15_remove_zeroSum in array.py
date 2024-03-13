class Solution:
    def removeZeroSum(self,arr):
        lst = []
        n = len(arr)
        for i in range(n + 1):
            for j in range(i , n):
                if arr[i] - arr[j] != 0:
                    lst.append(arr[j])
        return lst

if __name__ == "__main__":
    obj = Solution()
    array = list(map(int,input().split()))
    result = obj.removeZeroSum(array)
    print(result)
