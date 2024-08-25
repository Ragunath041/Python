class Animal:
    def speak(self):
        pass
    def move(self):
        pass
class Dog(Animal):
    def speak(self):
        return ' Boww Boww..!!!'
    def move(self):
        return 'Dog move using its legs and hands'
class Bird(Animal):
    def speak(self):
        return ' Keeee Keeee..!!!'
    def move(self):
        return 'Bird move using its Wings by Flying'

if __name__ == '__main__':
    b = Bird()
    d = Dog()
    print(b.speak())
    print(b.move())
    print(d.speak())
    print(d.move())