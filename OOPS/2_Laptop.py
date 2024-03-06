class Laptop:
    price = None
    processor = None
    ram = None
    
    def hp(self):
        print("HP Laptop.....")
    def dell(self):
        print("DeLL Laptop....")
    def lenovo(self):
        print("Lenovo Laptop....")

HP = Laptop()
DELL = Laptop()
LENOVO = Laptop()

HP.price = 50000
DELL.price = 55000
LENOVO.price = 60000

HP.processor = "RYZEN - 5"
DELL.processor = "RYZEN - 7"
LENOVO.processor = "INTEL - 9"

HP.ram = "4gb"
DELL.ram = "8gb"
LENOVO.ram = "16gb"

HP.hp()
print(f"Price : {HP.price} \nProcessor : {HP.processor} \nRAM : {HP.ram} \n")

DELL.hp()
print(f"Price : {DELL.price} \nProcessor : {DELL.processor} \nRAM : {DELL.ram} \n")

LENOVO.hp()
print(f"Price : {LENOVO.price} \nProcessor : {LENOVO.processor} \nRAM : {LENOVO.ram} \n")