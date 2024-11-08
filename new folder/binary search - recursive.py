def binarysearch(arr , low , high , k):
    if low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            return binarysearch(arr , mid + 1 , high , k)
        else:
            return binarysearch(arr , low , mid - 1 , k)
    else:
        return 0

if __name__ == "__main__":
    lst = list(map(int,input().split()))
    k = int(input())
    found = binarysearch(lst , 0 , len(lst) - 1 , k)
    if found:
        print(f"Found in {found}")
    else:
        print("Not Found")