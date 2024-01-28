# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
print("Enter the list element : ")
lst = [int(i) for i in input().split()]  #[8,1,2,2,3]
ans = []
for i in range(len(lst)):
    count = 0
    for j in range(len(lst)):
        if lst[i] > lst[j]:
            count += 1
    ans.append(count)
print("Answer = ",ans)
