class Solution:
    def two_sum(self , arr , k):
        ans = []
        for i in range(len(arr)):
            for j in range(i + 1 , len(arr)):
                if arr[i] + arr[j] == k:
                    ans.append(i)
                    ans.append(j)
        return ans



if __name__ == '__main__':
    obj = Solution()
    arr = list(map(int,input().split()))
    target = int(input())
    print("Sum of two elements is ",obj.two_sum(arr,target))
    