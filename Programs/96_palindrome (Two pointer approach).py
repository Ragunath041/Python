'''Return True if it is palindrom else False'''
def isPalindrome(s):
    i , j = 0 , len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
n = int(input())
for _ in range(n):
    s = input()
    print(isPalindrome(s))