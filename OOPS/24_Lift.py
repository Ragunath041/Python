class Solution:
    def Elavator(self , n , A , B):
        if A < B:
            return B * 10
        else:
            x = (n - 1) * 10
            for i in range(n - 2 , B - 1 , -1):
                x += 10
            return x

if __name__ == '__main__':
    obj = Solution()
    floor = int(input())
    start = int(input())
    distination = int(input())
    ans = obj.Elavator(floor , start , distination)
    print(ans)

'''
____
____
____  .
____
____  ..
'''