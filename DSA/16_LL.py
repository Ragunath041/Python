class Node:
    def __init__(self , item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

if __name__ == '__main__':
    obj = LinkedList()
    obj.head = Node(1)
    second = Node(2)
    obj.head.next = second
    second.next = None
    while obj.head != None:
        print(obj.head.item , end = " ")
        obj.head = obj.head.next