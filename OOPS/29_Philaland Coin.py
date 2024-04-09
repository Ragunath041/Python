import math
class Solution:
    def philaland(self , n):
        # x = 0
        # while (2 ** x) <= n:
        #     x += 1
        # return x

        return int(math.floor(math.log2(n) + 1))

if __name__ == "__main__":
    obj = Solution()
    n = int(input())
    ans = obj.philaland(n)
    print(ans)


# import math
# print(int(math.floor(math.log2(int(input())) + 1)))