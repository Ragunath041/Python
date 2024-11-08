B = "geeksforgeeks"
mapp = {}
for i in range(len(B)):
    if B[i:] not in mapp:
        mapp[B[i:]] = 1
    else:
        mapp[B[i:]] += 1
print(mapp)

"gksrek"