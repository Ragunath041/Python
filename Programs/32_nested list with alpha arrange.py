ans = []
score = []
for i in range(int(input())):
    temp1=input()
    temp2=float(input())
    ans.append([temp1,temp2])
    score.append(temp2)
sort = sorted(list(set(score)))
for x,y in sorted(ans):
    if y == sort:
        print(x)
