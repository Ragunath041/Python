lst = list(map(int,input("Enter the element :").split()))
target = int(input("Enter the Target Element :"))
for i in lst:
    if i+i == target:
        print(i)