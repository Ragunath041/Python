class Solution:
    def camel_case(self , s):
        s = s.title()
        lst = list(filter(lambda a : a.isalpha() , s))
        return ''.join(lst)
if __name__ == "__main__":
    obj = Solution()
    string = input()
    ans = obj.camel_case(string)
    print(ans)