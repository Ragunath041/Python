def findKthNumber(n , k):
    curr = i = 1
    def helper(curr):
        r = 0 
        nei = curr + 1
        while curr <= n:
            r += min(nei , n + 1) - curr
            curr *= 10
            nei  *= 10
        return r
    while i < k:
        s = helper(curr)
        if i + s <= k:
            curr += 1
            i += s
        else:
            curr *= 10
            i += 1
    return curr


print(findKthNumber(13 , 2))