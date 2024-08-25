''' 
Input:
arr = [1 , 4 , 10 , 16 , 20]
target = 26
Output:
10 16
'''

def TargetSum(arr , k):
    ans = []
    i , j = 0 , 1
    while i < j:
        if arr[i] + arr[j] != k:
            i += 1
            j += 1
        ans.append(arr[i])
        ans.append(arr[j])
    return ans
arr = list(map(int,input().split()))
k =  int(input())
print(TargetSum(arr , k))