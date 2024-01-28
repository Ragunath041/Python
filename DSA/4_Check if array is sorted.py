# input = [1,2,3,4,5]
# output : "Yes" if it sorted or "No"
def Is_sorted(arr , n):
    for i in range(1,n):
        if arr[i] >= arr[i - 1]:
            return True
            break
        else:
            return False
    return True

arr = list(map(int,input().split()))
n = len(arr)
print(Is_sorted(arr,n))
