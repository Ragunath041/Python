class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_level_order(arr, root, i, n):
    # Base case for recursion
    if i < n:
        if arr[i] is not None:
            temp = Node(arr[i])
            root = temp

            # Insert left child
            root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

            # Insert right child
            root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

# Example list
arr = [5,6,8,3,2,1]
n = len(arr)
root = insert_level_order(arr, None, 0, n)

# To check the result, we can do an inorder traversal
def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

# Print the inorder traversal of the tree
inorder_traversal(root)
