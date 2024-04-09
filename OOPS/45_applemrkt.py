class Solution:
    def helper_fun(self , n , m1 , p1 , m2 , p2):
        min_value = float('inf')
        for i in range(n // m1 + 1):
            remainder = n - i * m1
            if remainder % m2 == 0:
                cost = p1 * i + p2 * (remainder // m2)
                min_value = min(min_value , cost)
        return min_value

if __name__ == '__main__':
    obj = Solution()
    total_apples = int(input())
    no_apples_A_lots , A_lots_price = map(int, input().split())
    no_apples_B_lots , B_lots_price = map(int, input().split())
    result = obj.helper_fun(total_apples , no_apples_A_lots , A_lots_price , no_apples_B_lots , B_lots_price)
    print(result)