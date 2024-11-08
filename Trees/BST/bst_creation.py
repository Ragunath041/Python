class Node:
    def __init__(self , value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self , value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.helper(self.root , value)
    
    def helper(self , root , value):
        if value < root.value:
            if root.left is None:
                root.left = Node(value)
            else:
                self.helper(root.left , value)
        else:
            if root.right is None:
                root.right = Node(value)
            else:
                self.helper(root.right , value)
    def inorder(self , root):
        if self.root is not None:
            self.inorder(root.left)
            print(root.data , end = ' ')
            self.inorder(root.right)
    def preorder(self , root):
        if self.root is not None:
            print(root.data , end = " ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self , root):
        if self.root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data , end = " ")


if __name__ == '__main__':
    tree = Tree()
    lst = list(map(int , input().split()))
    for i in lst:
        tree.insert(i)
    print("Traversal Type...\n1.Inorder\n2.Postorder\n3.preorder")
    ch = int(input("Enter yr choice : "))
    match ch:
        case 1:
            tree.inorder(tree.root)
        case 2:
            tree.postorder(tree.root)
        case 3:
            tree.preorder(tree.root)
        case _ :
            print("Wrong Value...")