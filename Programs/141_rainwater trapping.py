class Solution:
    def trappingWater(self, arr):
        n = len(arr)
        prefixMax = []
        prefixMax.append(arr[0])
        suffixMin = []
        suffixMin.append(arr[0])
        for i in range(1 , n - 1):
            prefixMax.append(max(prefixMax[i - 1] , arr[i]))
            suffixMin.append(min(suffixMin[i - 1] , arr[i]))
        sol = 0
        for i in range(n):
            if arr[i] < prefixMax[i] and arr[i] < suffixMin[i]:
                sol += min(prefixMax[i] , suffixMin[i]) - arr[i]
        return sol
arr =  [8,8,2,4,5,5,1]
obj = Solution()
print(obj.trappingWater(arr))