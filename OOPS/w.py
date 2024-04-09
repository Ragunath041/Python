class Solution:
    def makeGood(self, s: str) -> str:
        q = []
        for c in s:
            cs = c.swapcase()
            if q and q[-1] == cs:
                q.pop()
            else:
                q.append(c)
        return ''.join(q)

# Example usage:
sol = Solution()
result = sol.makeGood("leEeetcode")
print(result)  # Output: "leetcode"
