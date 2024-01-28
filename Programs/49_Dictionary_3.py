my_dict = {}
for i in range(int(input("Enter the Length of the DICTIONARY :"))):
    Name = str(input(f"Enter the Name of {i}'s person :"))
    Salary = int(input(f"Enter Salary of {i}'s person :"))
    my_dict[Name] = Salary
if my_dict[Name] < 5000:
    print("These are all the members who have the salary greater than 5000 : ",my_dict)
