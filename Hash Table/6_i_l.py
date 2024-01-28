# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"

s = "codeleet"
ind = [4,5,6,7,0,2,1,3]
sort = sorted(ind)
s_list = list(s)
d = dict(zip(ind,s_list))
for i in sort:
    print(d[i],end="")