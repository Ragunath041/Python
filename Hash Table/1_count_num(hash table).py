n = int(input("Length :"))
arr = list(map(int,input().split()))
target = int(input("Enter the number to be search :"))
hashing = {}

for i in arr:
    if i in hashing:
        hashing[i] += 1
    else:
        hashing[i] = 1
        
if target in hashing:
    print(f"{target} is present {hashing[target]} times")
else:
    print(0)