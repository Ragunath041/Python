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
    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next
if __name__ == "__main__":
    node1 = Node("A")
    linkedlist = LinkedList()
    linkedlist.insert(node1)

    node2 = Node("B")
    linkedlist.insert(node2)

    node3 = Node("C")
    linkedlist.insert(node3)

    linkedlist.traverse()
