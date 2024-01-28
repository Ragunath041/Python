# SAMPLE INPUT_1:
# INPUT=6
# OUTPUT=10 -5 7 -3 2 -8

# SAMPLE INPUT_2:
# INPUT=6
# OUTPUT=5 -2 3 -1 6 -4
a=int(input("Enter limit:"))
arr=[]
sum=0
for i in range(1,a+1):
    b=int(input())
    arr.append(b)
for x in arr:
    if x%2!=0:
        sum+=x
print(sum)