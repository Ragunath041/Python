class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self , data):
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)
    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data , end = " ")
            current_node = current_node.next
    def delete(self , data):
        curr = self.head
        if curr is not None and curr.data == data:
            self.head = curr.next
        else:
            while curr is not None and curr.next is not None:
                if curr.next.data == data:
                    curr.next = curr.next.next
                    return 
                curr = curr.next


if __name__ == "__main__":
    obj = LinkedList()
    n = int(input("Range : "))
    for i in range(n):
        inp = int(input())
        obj.insert(inp)
    d = int(input("Delete : "))
    obj.delete(d)
    obj.display()