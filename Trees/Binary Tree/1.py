class BinaryTree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    def inserting(self , val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = BinaryTree(val)
                else:
                    self.left.inserting(val)
            else:
                if self.right is None:
                    self.right = BinaryTree(val)
                else:
                    self.right.inserting(val)
        else:
            self.val = val

    def printt(self):
        ch = int(input("1.Pre-order\n2.post-order\n3.in-order\n4.normal print:\n"))
        match ch:
            case 1:
                def pre_oder(self):
                    if val is not None:
                        print(self.val , end = " ")
                        self.pre_oder(self.left)
                        self.pre_oder(self.right)
            case 2:
                def post_order(self):
                    if val is not None:
                        self.post_order(self.left)
                        self.post_order(self.right)
                        print(self.val , end = " ")
            case 3:
                def in_order(self):
                    if self.val is not None:
                        self.in_order(self.left)
                        print(self.val , end = " ")
                        self.in_order(self.right)
            case _:
                    if self.left:
                        self.left.printt()
                    print(self.val , end = " "),
                    if self.right:
                        self.right.printt()
if __name__ == "__main__":
    root = BinaryTree(12)
    root.inserting(6)
    root.inserting(14)
    root.inserting(3)
    root.printt()