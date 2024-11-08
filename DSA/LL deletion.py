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
            while curr.next:
                curr = curr.next
            curr.next = nodee
    def printt(self):
        curr = self.head
        while curr:
            print(curr.data , end = " ")
            curr = curr.next
    def deleting(self):
        curr = self.head


if __name__ == '__main__':
    a = Node('A')
    linkedlist = LinkedList()
    linkedlist.insert(a)
    b = Node('B')
    linkedlist.insert(b)
    c = Node('C')
    linkedlist.insert(c)
    linkedlist.printt()