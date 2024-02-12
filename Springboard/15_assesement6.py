def calculate(a , b):
    while a != b:
        if a > b:
            return calculate(a - b , b)
        else:
            return calculate(a , b - a)
    return a


print(calculate(10 , 55))
print(calculate(60 , 30))
print(calculate(27 , 45))
print(calculate(45 , 20))