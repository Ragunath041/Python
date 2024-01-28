# a, b, c = input().split()
# lst = list(a)
# if b in lst:
#     index = lst.index(b)
#     lst.remove(b)
#     lst.insert(index, c)
# print(int(lst))
a, b, c = input().split()
lst = list(a)

print("Original list:", lst)

if b in lst:
    index = lst.index(b)
    lst.remove(b)
    lst.insert(index, c)

updated_list = int("".join(lst))
print("Updated list:", updated_list)
print("Removed element:", b)
print("Inserted element:", c)
