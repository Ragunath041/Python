class Node:
    def __init__(self , data):
        self.data = data
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
        if value < root.data:
            if root.left is None:
                root.left = Node(value)
            else:
                self.helper(root.left , value)
        else:
            if root.right is None:
                root.right = Node(value)
            else:
                self.helper(root.right , value)

    def bstHelper(self, root , mini , maxi):
        if root is None:
            return True
        if root.data < mini or root.data > maxi:
            return False
        return (self.bstHelper(root.left , mini , root.data - 1) and self.bstHelper(root.right , root.data + 1 , maxi))
    def isbst(self , root):
        if self.bstHelper(root , float('-inf') , float('inf')):
            return True
        else:
            return False
if __name__ == '__main__':
    tree = Tree()
    lst = list(map(int , input().split()))
    for i in lst:
        tree.insert(i)
    if(tree.isbst(tree.root)):
        print("Its a Binary Search Tree")
    else:
        print("Not a Binary Search Tree")