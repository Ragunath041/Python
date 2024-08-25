from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck):
        dq = deque()    
        for i in reversed(sorted(deck)):
            dq.rotate()
            dq.appendleft(i)
        return list(dq)
if __name__ == '__main__':
    obj = Solution()
    lst = list(map(int,input().split()))
    print(obj.deckRevealedIncreasing(lst))