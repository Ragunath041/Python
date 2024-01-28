import math
def isPerfectSquare(number):
    if(math.sqrt(number) == math.floor(math.sqrt(number))):
        return number
    else:
        return 0
n = int(input())
sum = 0
arr1 = []
for i in range(0,n):
    temp = int(input())
    arr1.append(temp)
for i in range(0,n):
    sum = sum + isPerfectSquare(arr1[i])
print(sum)
# import math
# def sqart(a):
#     if(math.sqrt(a)==math.floor(math.sqrt(n))):
#         return a
#     else:
#         return 0
# n=int(input())
# arr=[]
# sum=0
# for i in range(0,n):
#     temp=int(input())
#     arr.append(temp)
# for i in range(0,n):
#     sum+=sqart(arr[i])
# print(sum)