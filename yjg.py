# '''
# Input: s = "leetcode", k = 2
# Output: 6
# Explanation: The operations are as follows:
# - Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
# - Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
# - Transform #2: 33 ➝ 3 + 3 ➝ 6
# Thus the resulting integer is 6.
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
#  'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
# '''
# class Solution:
#     def getLucky(self, s , k):
#         x = 1
#         mapp = {}
#         x = 1
#         for _ in range(97 , 123):
#             mapp[chr(_)] = x
#             x += 1
#         def helper(s):
#             summ = 0
#             for i in range(len(ss)):
#                 summ += int(ss[i])
#             return summ
#         ss = ""
#         for i in range(len(s)):
#             ss += str(mapp[s[i]])
#         while k > 0:
#             q = ss
#             sol = helper(q)
#             k -= 1
#         return sol

        
# obj = Solution()
# s = "leetcode"
# k = 2
# print(obj.getLucky(s , k))


# '''
# Input: s = "iiii", k = 1
# Output: 36
# Explanation: The operations are as follows:
# - Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
# - Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
# Thus the resulting integer is 36.
# '''

class Solution:
    def canVisitAllRooms(self, rooms):
        visited = [0 for _ in range(len(rooms))]
        visited[0] = 1
        for rm in rooms:
            if rm:
                for j in range(len(rm)):
                    if not visited[rm[j]]:
                        visited[rm[j]] = 1
        print(visited)
        return True
obj = Solution()
rooms = [[1],[2],[3],[]]
print(obj.canVisitAllRooms(rooms))