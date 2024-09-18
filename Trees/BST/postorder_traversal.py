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
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data , end = " ")
if __name__ == "__main__":
    root = None
    lst = list(map(int,input().split()))
    for i in lst:
        root = insert(root , i)
    postorder(root)