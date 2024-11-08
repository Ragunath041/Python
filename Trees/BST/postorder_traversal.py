class Node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    def insert(self , data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.helper(self.root , data)
    def helper(self , root , data):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self.helper(root.left , data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                self.helper(root.right , data)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data , end = " ")

if __name__ == '__main__':
    tree = Tree()
    lst = list(map(int , input().split()))
    for i in lst:
        tree.insert(i)
    postorder(tree.root)