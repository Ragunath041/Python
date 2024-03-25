class Solution:
    # def fact(self , n):
    #     if n == 0 or n == 1:
    #         return n
    #     elif n == 2:
    #         return 2
    #     else:
    #         return n * self.fact(n - 1)
    # def trailingZeroes(self , n):
    #     factorial = self.fact(n)
    #     str_value = str(factorial)[::-1]
    #     count = 0
    #     for i in str_value:
    #         if i == '0':
    #             count += 1
    #             continue
    #         elif i != 0:
    #             break
    #     return count

    def trailingZeroes(self , n):
        count = 0
        if n == 0:
            return 0
        else:
            while n >= 1:
                n //= 5
                count += n
        return count

if __name__ == "__main__":
    obj = Solution()
    n = int(input())
    ans = obj.trailingZeroes(n)
    print(ans)