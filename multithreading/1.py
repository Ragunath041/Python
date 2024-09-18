import threading
import time

def adding(a , b):
    time.sleep(5)
    print("Adding " , a + b)
def multiply(a , b):
    time.sleep(3)
    print("Multi " , a * b)
def subtracting(a , b):
    time.sleep(1)
    print("subtract " , a - b)
a = threading.Thread(target = adding(10 , 2))
b = threading.Thread(target = multiply(12 , 0))
c = threading.Thread(target = subtracting(100 , 50))