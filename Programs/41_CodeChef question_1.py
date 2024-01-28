def maxof_three(x, y, z):
    return sorted([x, y, z], reverse=True)[:2]

for _ in range(int(input())):
    values = input().split()
    a1, a2, a3, b1, b2, b3 = map(int, values)
    a = sum(maxof_three(a1, a2, a3))
    b = sum(maxof_three(b1, b2, b3))
    
   
    if  a > b:
        print("Alice")
    elif b > a:
        print("Bob")
    else:
        print("Tie")
