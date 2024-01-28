import math
phi = (1 + math.sqrt(5))/2
def fibo(n):
      if n == 0 or n == 1:
            return n
      else:
            return ((phi) ** n - (-phi) ** (-n)) // math.sqrt(5)
n = int(input())
ans = int(fibo(n))
print(f"Fibonacci of {n} = {ans}")