from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text):

        balloon = Counter('balloon')
        hashing = Counter(text)
        res = len(text)

        for i in balloon:
            res = min(res , hashing[i] // balloon[i])
        return res
obj = Solution()
s = 'ballllllllllllooooooooooon'
ans = obj.maxNumberOfBalloons(s)
print(ans)