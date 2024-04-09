class Solution:
    def remove_dup(self , n , arr):
        ans = []
        for i in range(n):
            if arr[i] not in ans:
                ans.append(arr[i])
        return ans
if __name__ == "__main__":
    obj = Solution()
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int,input().split()))
        ans = obj.remove_dup(n , arr)
        print(*ans)