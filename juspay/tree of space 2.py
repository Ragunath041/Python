from collections import deque

class Tree:
    def __init__(self, name, head=None):
        self.name = name
        self.head = head
        self.childrens = []
        self.islocked = False
        self.locked_descendants = 0  # Tracks count of locked descendants
        self.locked = -1

    def add(self, strs):
        for name in strs:
            self.childrens.append(Tree(name, self))

class Tree2:
    def __init__(self, name):
        self.val = Tree(name)
        self.mp = {}

    def buildTree(self, strs, n):
        q = deque([self.val])
        k = 1
        size = len(strs)
        while q:
            r = q.popleft()
            self.mp[r.name] = r
            b = []
            for i in range(k, min(size, k + n)):
                b.append(strs[i])
            r.add(b)
            for child in r.childrens:
                q.append(child)
            k = i + 1

    def update_ancestors(self, r, change):
        while r:
            r.locked_descendants += change
            r = r.head

    def lock(self, name, id):
        r = self.mp[name]
        if r.islocked or r.locked_descendants > 0:
            return False
        par = r.head
        while par:
            if par.islocked:
                return False
            par = par.head
        self.update_ancestors(r.head, 1)  # Increase locked count for ancestors
        r.islocked = True
        r.locked = id
        return True

    def upgrade(self, name, id):
        r = self.mp[name]
        if r.islocked or r.locked_descendants == 0:
            return False
        # Check if all locked descendants are by the same ID
        for child in r.childrens:
            if not self.check_descendant_lock(child, id):
                return False
        # Unlock all descendants and lock the current node
        self.unlock_descendants(r, id)
        return self.lock(name, id)

    def check_descendant_lock(self, node, id):
        if node.islocked:
            return node.locked == id
        for child in node.childrens:
            if not self.check_descendant_lock(child, id):
                return False
        return True

    def unlock_descendants(self, node, id):
        if node.islocked and node.locked == id:
            self.unlock(node.name, id)
        for child in node.childrens:
            self.unlock_descendants(child, id)

    def unlock(self, name, id):
        r = self.mp[name]
        if not r.islocked or r.locked != id:
            return False
        self.update_ancestors(r.head, -1)  # Decrease locked count for ancestors
        r.islocked = False
        r.locked = -1
        return True

# Example of usage remains the same as before
size = int(input())
m = int(input())
testcases = int(input())
a = list(map(str, input().split()))
tree = Tree2(a[0])
tree.buildTree(a, m)
for _ in range(testcases):
    type_, name, id_ = input().split()
    id_ = int(id_)
    if type_ == '1':
        print("true" if tree.lock(name, id_) else "false")
    elif type_ == '2':
        print("true" if tree.unlock(name, id_) else "false")
    elif type_ == '3':
        print("true" if tree.upgrade(name, id_) else "false")
