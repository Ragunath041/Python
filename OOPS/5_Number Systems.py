class NumberSystems:
    def __init__(self):
        self.result = ''

    def binary_conversion(self , n):
        self.result = ''
        temp = n
        while temp != 0:
            x = temp % 2
            self.result += str(x)
            temp //= 2
        return self.result[::-1]
    
    def octal_conversion(self , n):
        self.result = ''
        temp = n
        while temp != 0:
            x = temp % 8
            self.result += str(x)
            temp //= 8
        return self.result[::-1]

    def hexa_decimal(self , n):
        self.result = ''
        temp = n
        values = {
            10 : 'A',
            11 : 'B',
            12 : 'C',
            13 : 'D',
            14 : 'E',
            15 : 'F'
        }
        while temp != 0:
            x = temp % 16
            if x >= 10:
                self.result += values[x]
            else:
                self.result += str(x)
            temp //= 16
        return self.result[::-1]

obj = NumberSystems()
n = int(input("Enter the Number : "))
print("DECIMAL TO BINARY - 1\nDECIMAL TO OCTAL - 2\nDECIMAL TO HEXADECIMAL - 3")
x = int(input("Enter the Choice :"))

if x == 1:
    print(obj.binary_conversion(n))
elif x == 2:
    print(obj.octal_conversion(n))
elif x == 3:
    print(obj.hexa_decimal(n))
else:
    print(-1)
