my_dict = dict(
    a = 10,
    b = 20,
    c = 30,
    d = 40,
    e = 50
)
# print(f"The Actual DICTIONARY IS {my_dict}")
# print("The Length of the is",len(my_dict));
# print(my_dict['a']+my_dict['e'])
for i in my_dict:
    print(my_dict[i]%3==0)