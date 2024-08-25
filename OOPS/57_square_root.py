class SquareRoot:
    def sqr_root(self , n):
        a = n / 2
        b = 0
        while a != b:
            b = a
            a = (n / b + b) / 2
        return int(a)

if __name__ == '__main__':
    obj = SquareRoot()
    n = int(input("Enter the Number to Find Square Root : "))
    print(obj.sqr_root(n))