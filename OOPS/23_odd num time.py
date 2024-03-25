from collections import Counter
n = int(input())
lst = list(map(int,input().split()))
count = Counter(lst)

for i , j in count.items():
    if j % 2 != 0:
        print(i)