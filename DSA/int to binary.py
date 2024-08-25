n = 35
binary = ""
while n > 0:
    binary = str(n % 2) + binary
    n //= 2
ans = "".join("1" if i == "0" else "0" for i in binary)
print(ans)