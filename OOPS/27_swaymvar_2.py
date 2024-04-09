class Solution:
    def  make_same(self, n ,bride , groom):
        x , c = "" , 0
        for i in range(n):
            for j in range(n):
                if bride[i] == groom[j]:
                    bride[i] = x
                    groom[j] = x
                    break
            if bride[i] != x:
                break
        for _ in range(n):
            if bride[_] != x:
                c += 1
        return c

if __name__ == "__main__":
    obj = Solution()
    n = int(input())
    bride = list(map(str,input().split()))
    groom = list(map(str,input().split()))
    ans = obj.make_same(n , bride , groom)
    print(ans)
