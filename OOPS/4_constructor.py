class Laptop:
    def __init__(self):
        self.name = None
        self.price = None
        self.processor = None
        self.ram = None
    def display(self):
        print(f"Name : {hp.name}\nPrice : {hp.price}\nProcessor : {hp.processor}\nRAM : {hp.ram}")

hp = Laptop()
hp.name = "HP Laptop"
hp.price = 50000
hp.processor = "Ryzen - 5"
hp.ram = "8gb"

hp.display()