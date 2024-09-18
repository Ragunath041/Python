class Tree:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None
def insert(root , key):
    if root is None:
        return Tree(key)
    if key < root.data:
        root.left = insert(root.left , key)
    else:
        root.right = insert(root.right , key)
    return root
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data , end = " ")
        inorder(root.right)
if __name__ == "__main__":
    root = None
    lst = list(map(int,input().split()))
    for i in lst:
        root = insert(root , i)
    inorder(root)
    