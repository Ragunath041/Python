def swap(a , b):
    temp = a
    a = b
    b = temp
def heapify(arr , n , i):
    large = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        large = l
    if r < n and arr[large] < arr[r]:
        large = r
    if large != i:
        temp = arr[i]
        arr[i] = arr[large]
        arr[large] = temp
        heapify(arr , n , large)
def heap_sort(arr , n):
    for i in range(n // 2 , -1 , -1):
        heapify(arr , n , i)
    for j in range(n - 1 , 0 , -1):
        temp = arr[j]
        arr[j] = arr[0]
        arr[0] = temp
        heapify(arr , j , 0)
arr = [34, 12, 45, 23, 11, 56, 78, 90, 34, 12, 45, 23, 11, 56, 78, 90]
n = len(arr)
heap_sort(arr , n)
print(arr)
# [11, 11, 12, 12, 23, 23, 34, 34, 45, 45, 56, 56, 78, 78, 90, 90]
