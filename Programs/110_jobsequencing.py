class Job:
    def __init__(self , id , profit , deadline):
        self.id = id
        self.profit = profit
        self.deadline = deadline
    
n = int(input())
id = [_ for _ in range(1 , n + 1)]
for _ in range(n):
    profit , deadline = map(int,input().split())
    