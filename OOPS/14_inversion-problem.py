class Inversion:
    def inversionOfarray(self , n , arr):
        count = 0
        lat = []
        lst = []
        for i in range(n + 1):
            for j in range(i , n):
                if arr[i] > arr[j]:
                    lat.append(arr[i])
                    lst.append(arr[j])
                    count += 1
        return count
if __name__ == '__main__':
    obj = Inversion()
    n = int(input())
    arr = list(map(int,input().split()))
    print(obj.inversionOfarray(n , arr))