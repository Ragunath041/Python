s = "Hello how are you Contestant"
k = 4
lst = list(s.split(" "))
if k > len(lst):
    print(s)
else:
    arr = []
    for i in range(k):
        arr.append(lst[i])
    print(" ".join(i for i in arr))