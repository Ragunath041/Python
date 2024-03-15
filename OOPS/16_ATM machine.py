class Solution:
    def ATMmachine(self ,n , amt , hun , t_hun , f_hun , tho):
        
        max_notes = 0           
        for i in range(hun + 1):
            for j in range(t_hun + 1):
                for k in range(f_hun + 1):
                    for l in range(tho + 1):
                        total_amount = i * 100 + j * 200 + k * 500 + l * 1000
                        total_notes = i + j + k + l
                        if total_amount == amt and total_notes <= n and total_notes > max_notes:
                            max_notes = total_notes
        return max_notes

if __name__ == '__main__':
    n = int(input())
    amount = int(input())
    hunderd = int(input())
    two_hundered = int(input())
    five_hundered = int(input())
    thousand = int(input())
    obj = Solution()
    ans = obj.ATMmachine(n , amount , hunderd , two_hundered , five_hundered , thousand)
    print(ans)
