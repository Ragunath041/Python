# def isSafe(visited , i):
#     return not visited[i]

# def permutaions(n , s , ans , visited , ind):
#     sol = ""
#     if ind == n:
#         # print(*ans)
#         for i in ans:
#             sol += i
#         print(sol)
#     else:
#         for i in range(n):
#             if isSafe(visited , i):
#                 ans[ind] = s[i]
#                 visited[i] = True
#                 permutaions(n , s , ans , visited , ind + 1)
#                 visited[i] = False

# s = input()
# N = len(s)
# visited = [False] * N
# ans = [None] * N
# permutaions(N , s , ans , visited , 0)

# from itertools import permutations
# lst = ["foo","bar"]
# a = ["".join(_) for _ in list(permutations(lst))]

# def substring(s , n):
#     for i in range(len(s) - n + 1):
#         yield  s[i : i + n]
# def substrings(s , n , l,st):
#     for i in range(l):
#         for j in range(i , n + 1):
#             st += s[i]
#         return st

# s = "barfoothefoobarman"
# n = len(s)
# k = 6
# arr = []
# ss = ""
# substrings(s , k , n , ss)
# print(ss)

def substrings_of_size_k(s, k):
    substrings = []
    for i in range(len(s) - k + 1):
        substrings.append(s[i:i+k])
    return substrings

# Example usage
s = "barfoothefoobarman"
k = 6
result = substrings_of_size_k(s, k)
print(result)  # Output: ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh']
