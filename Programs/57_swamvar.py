# n = int(input())
# s1 = str(input())
# s2 = str(input())
# s1_lst = list(s1)
# s2_lst = list(s2)
# same = 0
# not_same = 0
# for i in range(len(s1)):
#     for j in range(len(s2)):
#         if s1_lst[i] == s2_lst[j]:
#             same += 1
#         else:
#             not_same += 1
# print(same)
# print(not_same)
n = int(input())
s1 = str(input())
s2 = str(input())
s,ns = 0,0
for i in range(n):
    if s1[i] == s2[i]:
        s += 1
    elif s1[i] != s2[i]:
        ns += 1
print(s)
print(ns)