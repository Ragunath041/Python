class Solution:
    def swayamvar(self , n , bridge , groom):
        i = 0
        while i < n:
            d = groom.find(bridge[0])
            if d < 0:
                break
            groom = groom[d + 1:] + groom[:d]
            bridge = bridge[1:]
            i += 1
        return len(bridge)
            

if __name__ == '__main__':
    obj = Solution()
    n = int(input())
    bridge = input()
    groom  = input()
    ans = obj.swayamvar(n , bridge , groom)
    print(ans)
