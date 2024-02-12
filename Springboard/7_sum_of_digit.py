def sum_of_digit(n):
    sum = 0
    while n != 0:
        remainder = n % 10
        sum += remainder
        n //=10
    return sum
n = 123
print(sum_of_digit(n))