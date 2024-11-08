class Node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def insert(self , data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return
        else:
            Queue = [self.root]
            while Queue:
                temp = Queue.pop(0)
                if not temp.left:
                    temp.left = newNode
                    return 
                else:
                    Queue.append(temp.left)
                if not temp.right:
                    temp.right = newNode
                    return 
                else:
                    Queue.append(temp.right)
    def inorder(self , root):
        if root is not None:
            self.inorder(root.left)
            print(root.data , end = " ")
            self.inorder(root.right)
if __name__ == '__main__':
    tree = Tree()
    lst = list(map(int,input().split()))
    for i in lst:
        tree.insert(i)
    tree.inorder(tree.root)