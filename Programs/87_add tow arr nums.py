class Sum_arr:
    def addTwonums(self , arr1 , arr2):
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]
        a = int("".join(map(str,arr1)))
        b = int("".join(map(str,arr2)))
        add = a + b
        lst = [int(i) for i in str(add)]

        return lst[::-1]

# l1 = list(map(int,input().split()))
# l2 = list(map(int,input().split()))

l1 = [2,4,3]
l2 = [5,6,4]

obj = Sum_arr()
ans = obj.addTwonums(l1 , l2)
print(ans)