arr = [4,5,6,7,0,2,1,3]
hash_table = {}
for i in range(len(arr)):
    if arr[i] in hash_table:
        hash_table[arr[i]] += 1
    else:
        hash_table[arr[i]] = 1
print(hash_table)
