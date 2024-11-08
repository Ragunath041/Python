class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
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

    def height(self, node):
        if node is None:
            return -1
        l_height = self.height(node.left)
        r_height = self.height(node.right)
        return 1 + max(l_height, r_height)

    def leftSubTree(self):
        if self.root is None or self.root.left is None:
            return 0
        return self.height(self.root.left)

    def rightSubTree(self):
        if self.root is None or self.root.right is None:
            return 0
        return self.height(self.root.right)
    
if __name__ == '__main__':
    tree = Tree()
    lst = list(map(int, input("Enter tree elements: ").split()))
    for i in lst:
        tree.insert(i)
    
    # Display heights of left and right subtrees
    print("Height of left subtree:", tree.leftSubTree())
    print("Height of right subtree:", tree.rightSubTree())
