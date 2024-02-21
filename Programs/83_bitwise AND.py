class Bitwise:
    def bitwiseAnd(self,a,b):
        i = 0
        while a != b:
            a >>= 1
            b >>= 1
            i += 1
        return a << i
left = int(input())
right = int(input())
obj = Bitwise()
ans = obj.bitwiseAnd(left , right)
print(ans)