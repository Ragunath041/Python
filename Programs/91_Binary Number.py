n = int(input("Enter the Number :"))
binary = ''

temp = n

while temp != 0:
    a = temp % 2
    binary += str(a)
    temp //= 2
print(binary[::-1])
