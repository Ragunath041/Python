# Input: words = ["leet","code"], x = "e"
# Output: [0,1]
# Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

n = int(input("Enter the Number choice for your Input.. Press 1 if it is Integer or press 2 if it is string :"))
if n == 1:
    # size = int(input("Enter the size of the element :"))
    int_lst = []
    for i in range(int(input("Enter the Size of the List :"))):
        temp = int(input())
        int_lst.append(temp)
        find_int = int(input("Enter the Number to Find in the array :"))
        for j in int_lst:
            if len(str(int_lst[i])) != 1:
                dubli_lst = list(str(int_lst[i]))
                for k in dubli_lst:
                    if find_int == dubli_lst[k]:
                        
    print(int_lst)
elif n == 2:
    str_lst = []
    for i in range(int(input("Enter the Size of the List :"))):
        temp = str(input())
        str_lst.append(temp)
    print(str_lst)
else:
    print("Out of Choice....!")