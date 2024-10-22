import itertools

class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        letters = [digit_to_letters[digit] for digit in digits]
        print(letters)
        return [''.join(p) for p in itertools.product(*letters)]
            
obj = Solution()
print(obj.letterCombinations('23'))

        