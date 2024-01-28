# input : arr = [1,2,3,4,5]
# output : [4,2]
def Slarge(arr,l):
    large = arr[0]
    second_large = -1
    for i in range(l):
        if arr[i] > large:
            second_large = large
            large = arr[i]
        else:
            if arr[i] < large and arr[i] > second_large:
                second_large = arr[i]
    return second_large

def Ssmaller(arr , l , x):
    small = arr[0]
    second_small = x
    for i in range(l):
        if arr[i] < small:
            second_small = small
            small = arr[i]
        else:
            if arr[i] > small and arr[i] < second_small:
                second_small = arr[i]
    return second_small





arr = [1,2,3,4,5]
n = len(arr)
a = Slarge(arr,n)
b = Ssmaller(arr,n,a)
print(f"[{a} , {b}]")