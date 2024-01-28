lst = []
n = int(input("Enter the size of a list :"))
for i in range(n):
    temp = int(input())
    lst.append(temp)
x = n/2
print("Original List : ",lst)
print("First Half :",lst[:x])
print("Second Half :",lst[x:])