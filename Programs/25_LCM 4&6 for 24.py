def find_common_multiples(a, b):
    common_multiples = []
    for i in range(1, max(a, b) + 1):
        if i % a == 0 and i % b == 0:
            common_multiples.append(i)
    return common_multiples

def find_lcm(a, b):
    lcm = (a * b) // find_gcd(a, b)
    return lcm

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = 4
num2 = 6

common_multiples = find_common_multiples(num1, num2)
lcm = find_lcm(num1, num2)

print(f"Common multiples of {num1} and {num2}: {common_multiples}")
print(f"Least Common Multiple (LCM) of {num1} and {num2}: {lcm}")
