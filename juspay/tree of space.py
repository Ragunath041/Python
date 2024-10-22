from collections import deque
class Tree:
    def __init__(self, name, head=None):
        self.name = name
        self.head = head
        self.childrens = []
        self.islocked = False
        self.bottom = set()
        self.locked = -1
    def add(self, strs):
        for name in strs:
            self.childrens.append(Tree(name, self))
class Tree2:
    def __init__(self, name):
        self.val = Tree(name)
        print(self.val)
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
    def update(self, r, current):
        while r:
            r.bottom.add(current)
            r = r.head
    def lock(self, name, id):
        r = self.mp[name]
        if r.islocked or len(r.bottom) > 0:
            return False
        par = r.head
        while par:
            if par.islocked:
                return False
            par = par.head
        self.update(r.head, r)
        r.islocked = True
        r.locked = id
        return True
    def upgrade(self, name, id):
        r = self.mp[name]
        if r.islocked or len(r.bottom) == 0:
            return False
        for it in r.bottom:
            if it.locked != id:
                return False
        par = r.head
        while par:
            if par.islocked:
                return False
            par = par.head
        st = r.bottom.copy()
        for it in st:
            self.unlock(it.name, id)
        self.lock(name, id)
        return True
    def unlock(self, name, id):
        r = self.mp[name]
        if not r.islocked or r.locked != id:
            return False
        par = r.head
        while par:
            par.bottom.discard(r)
            par = par.head
        r.islocked = False
        r.locked = -1
        return True
size = int(input())
m = int(input())
testcases = int(input())
a = list(map(str,input().split()))
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
        