class Solution:
    # def str_rev(self , s):
    #     rev = ''
    #     for i in s:
    #         rev += i
    #     #print(rev)
    #     return rev
    def non_vow(self , s):
        vowels = 'aeiou'
        string = ''
        for i in s:
            if  i not in vowels:
                string += i
        # if string == self.str_rev(string):
        if string == string[::-1]:
            return 'YES'
        else:
            return 'NO'
if __name__ == '__main__':
    obj = Solution()
    string = input()
    ans = obj.non_vow(string)
    print(ans)