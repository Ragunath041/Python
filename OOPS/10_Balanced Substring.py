class Solution:
    def BalancedSubstring(self, s):
        count = 0
        a = 0
        for i in range(len(s)):
            if s[i] == 'L':
                a += 1
            else:
                a -= 1
            if a == 0:
                count += 1
        return count

obj = Solution()
s = input("Enter a string: ")
ans = obj.BalancedSubstring(s)
print("Number of balanced substrings:", ans)
