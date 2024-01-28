fact = lambda x : 1 if x <= 1 else x * fact(x - 1)
n = int(input("Enter the number :"))
print(f"The factorial of {n} is : ",fact(n))