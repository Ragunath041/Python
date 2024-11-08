from collections import deque
class Tree:
    def __init__(self , name , head = None):
        self.name = name
        self.head = head
        self.childrens = []
        self.islocked = False
        self.bottom = set()
        self.locked = -1
class Tree2:
    def __init__(self , name):
        self.val = Tree(name)
        self.mapp = {}
    def building_tree(self , lst , n):
        qq = deque([self.val])
        k = 1
        


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    T = int(input())
    lst = list(map(str , input().split()))
    tree = Tree2(lst[0])
    tree.building_tree(lst , m)
    ans = []
    for _ in range(T):
        type_ , name , person_id = input().split()
        person_id = int(person_id)
        if type_ == '1':
            if tree.lock(name , person_id):
                ans.append(True)
            else:
                ans.append(False)
        elif type_ == '2':
            if tree.unlock(name , person_id):
                ans.append(True)
            else:
                ans.append(False)
        else:
            if tree.upgrade(name , person_id):
                ans.append(True)
            else:
                ans.append(False)