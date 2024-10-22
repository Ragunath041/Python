'''
Input: arr1 = [1,10,100], arr2 = [1000]
Output: 3
Input: arr1 = [10] , arr2 =[17, 11]
Output: 1
'''
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
pre_fix = set()
length = 0
for temp in arr2:
    s = str(temp)
    for i in range(1 , len(s) + 1):
        pre_fix.add(s[:i])
for temp in arr1:
    s = str(temp)
    if s in pre_fix and len(s) > length:
        length = len(s)
    else:
        for i in range(1 , len(s) + 1):
            if s[:i] in pre_fix and len(s[:i]) > length:
                length = len(s[:i])
print(length)