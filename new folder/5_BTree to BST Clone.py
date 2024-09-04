
class Tree:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.right = right
        self.left = left

def inserting(root , val):
    if root is None:
        return Tree(val)
    if val < root.val:
        root.left = inserting(root.left , val)
    if val > root.val:
        root.right = inserting(root.right , val)
    return root

def bstree(lst):
    if not lst:
        return 
    root = Tree(lst[0])
    for val in lst[1:]:
        if val is not None:
            root = inserting(root , val)
    return root

    dfs(root)
    return ans
def forming_tree(lst):
    if not lst:
        return None
    root = Tree(lst[0])
    q = [root]
    i = 1
    while i < len(lst):
        node = q.pop(0)
        if lst[i] is not None:
            node.left = Tree(lst[i])
            q.append(node.left)
        i += 1
        if lst[i] is not None:
            node.right = Tree(lst[i])
            q.append(node.right)
        i += 1
    return root
def post_order(root):
    ans = []
    def dfs(root):
        nonlocal ans
        if root is None:
            return 
        dfs(root.left)
        dfs(root.right)
        ans.append(root.val)
    dfs(root)
    return ans
inp = input().split()
lst = [int(i) if i != "None" else None for i in inp]
tree = forming_tree(lst)
post = post_order(tree)
bst = bstree(lst)
postBST = post_order(bst)
print(f"normal tree : {post}\nBST : {postBST}")