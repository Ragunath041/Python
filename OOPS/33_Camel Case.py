class Solution:
    def camel_case(self , s):
        s = s.title()
        return ''.join(filter(lambda a : a.isalpha() , s))

if __name__ == "__main__":
    obj = Solution()
    string = input()
    ans = obj.camel_case(string)
    print(ans)