class Tree:
    def __init__(self , data):
        self.data = data
        self.right = None
        self.left = None
def insert(root , key):
    new_node = Tree(key)
    if root is None:
        return new_node
    queue = []
    queue.append(root)
    while queue:
        n = queue.pop(0)
        if not n.left:
            n.left = new_node
            return root
        else:
            queue.append(n.left)
        if not n.right:
            n.right = new_node
            return root
        else:
            queue.append(n.right)
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