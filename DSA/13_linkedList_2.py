class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def inserting(self , data):
        demo_node = Node(data)
        if self.head is None:
            self.head = demo_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = demo_node
    def print_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data , end = '  ')
            current_node = current_node.next
if __name__ == '__main__':
    ll = LinkedList()
    arr = [1 , 2 , 3 , 4 , 5]
    for i in range(len(arr)):
        ll.inserting(arr[i])
    ll.print_list()
