class Solution:
    def alternate_sorting(self , arr):
        odd_numbers  = [i for i in arr if i % 2 != 0]
        even_numbers = [i for i in arr if i % 2 == 0]
        arr_altr = []
        i , j = 0 , 0
        while i < len(odd_numbers) and j < len(even_numbers):
            arr_altr.append(odd_numbers[i])
            arr_altr.append(even_numbers[j])
            i += 1
            j += 1
        return arr_altr
    
if __name__ == '__main__':
    obj = Solution()
    arr = list(map(int,input().split()))
    ans = obj.alternate_sorting(arr)
    print(ans)
