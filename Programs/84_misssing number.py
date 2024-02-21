class Missing:
    def missing_number(self , arr): #[0 , 1 , 3]
        lst = [i for i in range(0 , len(arr))] #[0 , 1, 2]
        a = 0
        for i in range(len(lst) + 1):
            if i in arr:
                continue
            else:
                a += i
        return lst , a
arr = list(map(int,input().split()))
obj = Missing()
ans = obj.missing_number(arr)
print(ans)