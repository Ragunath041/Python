class Solution:
    def  make_same(self, n ,bridge , groom):
        x , c = "" , 0
        for i in range(n):
            for j in range(n):
                if bridge[i] == groom[j]:
                    bridge[i] = x
                    groom[j] = x
                    break
            if bridge[i] != x:
                break
        for _ in range(n):
            if bridge[_] != x:
                c += 1
        return c

if __name__ == "__main__":
    obj = Solution()
    n = int(input())
    bridge = list(map(str,input().split()))
    groom = list(map(str,input().split()))
    ans = obj.make_same(n , bridge , groom)
    print(ans)
