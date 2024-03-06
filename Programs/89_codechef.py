def binary_numbers(num):
    return '{0:b}'.format(int(n))
def binary_sum(n):
    s = str(n)
    x = [int(i) for i in s]
    return sum(x)
        
for i in range(int(input())):
    n = int(input())
    x = binary_numbers(n)
    print('EVEN' if binary_sum(x) % 2 == 0 else "ODD")
