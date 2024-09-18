class Tree:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.right = right
        self.left = left
def forming_BT(lst):
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
        if lst[i] is not None and i < len(lst):
            node.right = Tree(lst[i])
            q.append(node.right)
        i += 1
    return root

def pre_order(root):
    ans = []
    def dfs(root):
        nonlocal ans
        if root is None:
            return
        ans.append(root.val)
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return ans

def in_order(root):
    ans = []
    def dfs(root):
        nonlocal ans
        if root is None:
            return 
        dfs(root.left)
        ans.append(root.val)
        dfs(root.right)
    dfs(root)
    return ans

def post_order(root):
    ans = []
    def dfs(root):
        if root is None:
            return 
        dfs(root.left)
        dfs(root.right)
        ans.append(root.val)
    dfs(root)
    return ans

inp = input().split()
lst = [int(i) if i != 'None' else None for i in inp]
# lst = [5,6,8,3,2,1]
tree = forming_BT(lst)
post_order = post_order(tree)
pre_order = pre_order(tree)
in_order = in_order(tree)
print(f"Post Oreder : {post_order}\nPre Order : {pre_order}\nIn Order : {in_order}")
