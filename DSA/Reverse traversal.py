class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self , nodee):
        if self.head is None:
            self.head = nodee
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = nodee
    def printt(self):
        curr = self.head
        while curr is not None:
            print(curr.data , end = "->")
            curr = curr.next
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp
        self.head = prev
        self.printt()

if __name__ == '__main__':
    a = Node('A')
    linkedlist = LinkedList()
    linkedlist.insert(a)
    b = Node('B')
    linkedlist.insert(b)
    c = Node('C')
    linkedlist.insert(c)
    d = Node('D')
    linkedlist.insert(d)
    linkedlist.reverse()

