def countOddXorPairs(arr):
    count = 0
    i , j = 0 , len(arr) - 1
    while j > 0:
        if (arr[i] ^ arr[j]) % 2 != 0:
            count += 1
            i += 1
        j -= 1
    return count
arr = [1,2,3]
print(countOddXorPairs(arr))  