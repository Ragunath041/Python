class Tree:
    def __init__(self , val = 0 , right = None , left = None):
        self.val = val
        self.right = right
        self.left = left
def helper(original , cloned , target):
    q = [(original , cloned)]
    while q:
        a , b = q.pop()
        if a.val == target:
            return b
        if a.left:
            q.append((a.left , b.left))
        if a.right:
            q.append((a.right , b.right))
    return None
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
inp = input().split()
lst = [int(i) if i != "None" else None for i in inp]
tree = forming_tree(lst)
cloned = tree
target = 3
ans = helper(tree , cloned , target)
print(ans.val)