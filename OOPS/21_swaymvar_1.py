class Solution:
    def swayamvar(self , n , bride , groom):
        i = 0
        while i < n:
            d = groom.find(bride[0])
            #print(d)
            if d < 0:
                break
            groom = groom[d + 1:] + groom[:d]
            bride = bride[1:]
            i += 1
        return len(bride)
            

if __name__ == '__main__':
    obj = Solution()
    n = int(input())
    bride = input()
    groom  = input()
    ans = obj.swayamvar(n , bride , groom)
    print(ans)
