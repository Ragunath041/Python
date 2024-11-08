def binarysearch(arr , low , high , target):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return 0
arr = list(map(int,input().split()))
target = int(input())
found = binarysearch(arr , 0 , len(arr) - 1 , target)
if found:
    print(f"Found at {found} position")
else:
    print("Not found...")