import bisect 

a = [3,5,1,4]

target = 2

i = bisect.bisect_right(a,target)

a.insert(i,target)

print(i)

jls_extract_var = print
jls_extract_var(a)