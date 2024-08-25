class Vehicle:
    def __init__(self , color , speed):
        self.color = color
        self.speed = speed
    def clr(self):
        print(f'This is {self.color} Color')
    def spd(self):
        print(f'This is {self.speed} km/hr')
class Car(Vehicle):
    def __init__(self , color , speed , brand):
        super().__init__(color , speed)
        self.brand = brand
    def brd(self):
        print(f'Brand : {self.brand}')

obj = Car('RED' , '134' , 'BMW')
obj.brd()
obj.clr()
obj.spd()
    