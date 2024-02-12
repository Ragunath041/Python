number = 121
temp = number
rev = 0
while number != 0:
    remainder = number % 10
    rev = rev * 10 + remainder
    number //= 10

print(temp)
print(rev)

if temp == rev:
    print("Y")
else:
    print("N")