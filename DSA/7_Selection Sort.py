print("SELECTION SORT ALGORITHM......")
lst = list(map(int,input("Enter the list numbers: ").split()))
length = len(lst)
for i in range(length):
    least_element = i
    for j in range(i+1 , length):
        if lst[j] < lst[least_element]:
            least_element = j
        lst[i] , lst[least_element] = lst[least_element] , lst[i]
print(lst)