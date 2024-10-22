from collections import defaultdict
words = list(map(str,input().split()))
# words = ["abc","ab","bc","b"]
D = defaultdict(int)
count = []
for ss in words:
    for i in range(1 , len(ss) + 1):
        D[ss[:i]] += 1
for ss in words:
    x = 0
    for i in range(1 , len(ss) + 1):
        x += D[ss[:i]]
    count.append(x)
print(count)