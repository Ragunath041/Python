import bisect
a = [1,2,3,4,5]
item_1 = 4
item_2 = 5
i = bisect.bisect_left(a,item_1)   
j = bisect.bisect_right(a,item_2)
a.insert(i,item_1)
a.insert(j,item_2)
print("Final List :",a)
print("Inserted Position for i : ",i)
print("Inserted Position for j : ",j)


