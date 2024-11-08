class Tree:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None


if __name__ == "__main__":
    root = Tree(10)
    root.left = Tree(5)
    root.right = Tree(6)
    root.left.left = Tree(4)
    root.left.right = Tree(8)
    root.right.right = Tree(20)
    root.right.left = Tree(12)
    print(f"Inorder Traversal : {root.inorder_traversal()}")
    # print(f"Preorder Traversal : {root.preorder_traversal()}")
    # print(f"Postorder Traversal : {root.postorder_traversal()}")