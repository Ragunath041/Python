class Tree:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right
def helper(root , low , high):
    summ = 0
    def dfs(root):
        nonlocal summ
        if root is None:
            return
        if root.val > low:
            dfs(root.left)
        if low <= root.val <= high:
            summ += root.val
        if root.val < high:
            dfs(root.right)
    dfs(root)
    return summ
def inserting_element(root , val):
    if root is None:
        return Tree(val)
    if val < root.val:
        root.left = inserting_element(root.left , val)
    else:
        root.right = inserting_element(root.right , val)
    return root

def forming_tree(lst):
    if not lst:
        return None
    root = Tree(lst[0])
    for val in lst[1:]:
        if val is not None:
            root = inserting_element(root , val)
    return root

lst = [10 , 5 , 15 , 3 , 7 , 13 , 18 , 1 , None , 6]
tree = forming_tree(lst)
low = 6
right = 10
# print(tree)
res = helper(tree , low , right)
print(res)