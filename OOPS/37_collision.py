import math
class Solution:
    def collision(self, cars):
        D = {}
        collision = 0        
        for x, y, v in cars:
            distance = math.sqrt(x**2 + y**2)        #ROOT((X2 - X1) ^2 + (Y2 - Y1)^2)
            time = distance / v
            #print(time)
            if time in D:
                D[time] += 1
            else:
                D[time] = 1
        for i in D.values():
            if i != 1:
                collision += (i * (i - 1)) // 2
        print(D)
        return collision
if __name__ == "__main__":
    obj = Solution()
    cars = int(input())
    car_list = []
    for _ in range(cars):
        lst = list(map(int, input().split()))
        car_list.append(lst)        
    ans = obj.collision(car_list)
    print(ans)