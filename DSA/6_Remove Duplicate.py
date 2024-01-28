# input : arr = [1,2,2,3,4,4,5]
# output : [1,2,3,4,5]
def rmd(arr,i):
    for j in range(1,len(arr)):
        if arr[j] == arr[i]:
            arr[i + 1] = arr[j]
            i+1
    return (i + 1)
arr = [1,2,2,3,4,4,5]
i = 0
print(rmd(arr,i))
