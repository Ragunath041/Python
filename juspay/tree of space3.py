from collections import deque
from threading import Lock, Thread

class Tree:
    def __init__(self, name, head=None):
        self.name = name
        self.head = head
        self.childrens = []
        self.islocked = False
        self.locked_descendants = 0  # Tracks count of locked descendants
        self.locked = -1
        self.lock = Lock()  # Lock for thread safety

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
            with r.lock:
                r.locked_descendants += change
            r = r.head

    def lock(self, name, id):
        r = self.mp[name]
        with r.lock:
            if r.islocked or r.locked_descendants > 0:
                return False
            par = r.head
            while par:
                with par.lock:
                    if par.islocked:
                        return False
                par = par.head
            self.update_ancestors(r.head, 1)
            r.islocked = True
            r.locked = id
        return True

    def upgrade(self, name, id):
        r = self.mp[name]
        with r.lock:
            if r.islocked or r.locked_descendants == 0:
                return False
            for child in r.childrens:
                if not self.check_descendant_lock(child, id):
                    return False
            self.unlock_descendants(r, id)
            return self.lock(name, id)

    def check_descendant_lock(self, node, id):
        with node.lock:
            if node.islocked:
                return node.locked == id
            for child in node.childrens:
                if not self.check_descendant_lock(child, id):
                    return False
        return True

    def unlock_descendants(self, node, id):
        with node.lock:
            if node.islocked and node.locked == id:
                self.unlock(node.name, id)
            for child in node.childrens:
                self.unlock_descendants(child, id)

    def unlock(self, name, id):
        r = self.mp[name]
        with r.lock:
            if not r.islocked or r.locked != id:
                return False
            self.update_ancestors(r.head, -1)
            r.islocked = False
            r.locked = -1
        return True

# Testing function for threading
def test_operations(tree, ops):
    for op in ops:
        type_, name, id_ = op
        id_ = int(id_)
        if type_ == '1':
            print("true" if tree.lock(name, id_) else "false")
        elif type_ == '2':
            print("true" if tree.unlock(name, id_) else "false")
        elif type_ == '3':
            print("true" if tree.upgrade(name, id_) else "false")

# Example usage
size = int(input())
m = int(input())
testcases = int(input())
a = list(map(str, input().split()))
tree = Tree2(a[0])
tree.buildTree(a, m)

# Collecting test cases
operations = []
for _ in range(testcases):
    type_, name, id_ = input().split()
    operations.append((type_, name, id_))

# Running operations in threads
num_threads = 4  # Number of threads
threads = []
for i in range(num_threads):
    ops_for_thread = operations[i::num_threads]  # Distribute operations across threads
    t = Thread(target=test_operations, args=(tree, ops_for_thread))
    t.start()
    threads.append(t)

for i in threads:
    i.join()