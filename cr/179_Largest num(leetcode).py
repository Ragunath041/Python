lst = list(map(int,input().split()))
str_list = [str(i) for i in lst]
str_list.sort(key = lambda x : x * 10 , reverse = True)
print(''.join(str_list))