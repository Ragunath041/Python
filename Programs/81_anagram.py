def anagram(a , b):
    count = 0
    if len(a) != len(b):
        return "Not a Anagram"
    for i in a:
        if i in b:
            count += 1
    if count == len(a):
        return "Yes Its an Anagram"
    else:
        return "Not a Anagram"
str_1 = input()
str_2 = input()
print(anagram(str_1 , str_2))