class Basic_Math:
    def adding(self , a , b):
        return a + b
    def subtracting(self , a , b):
        return a - b
    def multiple(self , a , b):
        return a * b
    def divid(self , a , b):
        return a // b
class Inter_Math(Basic_Math):
    def modulo(self , a , b):
        return a % b
    def percentage(self , a , b):
        return '{:.2f}%'.format((a / b) * 100)
    def cmplex(self , a , b):
        return f'{a} + {b}i'
    

obj = Inter_Math()
while True:
    a = int(input('A : '))
    b = int(input('B : '))
    choice = int(input("1. ADDITION\n2. SUBTRACTION\n3. MULTIPLICATION\n4. DIVISION\n5. MODULO\n6. PERCENTAGE\n7. COMPLEX\n8. EXIT\n"))
    if choice == 1:
        print(obj.adding(a , b))
    elif choice == 2:
        print(obj.subtracting(a , b))
    elif choice == 3:
        print(obj.multiple(a , b))
    elif choice == 4:
        print(obj.divid(a , b))
    elif choice == 5:
        print(obj.modulo(a , b))
    elif choice == 6:
        print(obj.percentage(a , b))
    elif choice == 7:
        print(obj.cmplex(a, b))
    else:
        break