import sys
class Memory:
    def memory(self):
        print("The Memory Allocation for Object-1 : ",sys.getsizeof(obj1))
    def addition(self,a,b):
        print("The Sum =",a+b," and it's Memory Allocation =",sys.getsizeof(obj2))
obj1 = Memory()
obj2 = Memory()
obj1.memory()
obj2.addition(10,20)