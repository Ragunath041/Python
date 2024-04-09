class Solution:
    def ATMmachine(self , n , h , t_h , f_h , th , amount):
        max_note = float("-inf")
        for i in range(h + 1):
            for j in range(t_h + 1):
                for k in range(f_h + 1):
                    for l in range(th + 1):
                        total_amount = (i * 100) + (j * 200) + (k * 500) + (l * 1000)
                        total_notes = i + j + k + l
                        if total_amount == amount and total_notes > max_note and total_notes <= n:
                            max_note = total_notes
        return max_note


if __name__ == '__main__':
    o = Solution()
    n = int(input())
    amount = int(input())
    h = int(input())
    t_h = int(input())
    f_h = int(input())
    th =  int(input())
    ans = o.ATMmachine(n , h , t_h , f_h , th , amount)
    print(f"Total Notes : {ans}")    
    




