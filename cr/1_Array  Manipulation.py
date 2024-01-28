lst = list(map(int,input().split()))

print(f"Default Array : {lst} ")

# Insertion

n = int(input("Enter the Number want to insert :"))

lst.append(n)

print(f"After Inserting {n} element inside the List, so the array is {lst}")

# insert at index

num = int(input("Enter the number : "))
i = int(input("Enter the Index want to Insert Element :"))

lst.insert(i,num)

print(f"After Inserting the number {num} at the index {i} then the list is {lst}")


# Delete

d = int(input("Enter the number to delete :"))
lst.remove(d)

print(f"after remove list is {lst}")

# delete at Index

di = int(input("Enter Index to del num:"))

del lst[di]

print(f"List after that : {lst}")