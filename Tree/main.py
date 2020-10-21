class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.cargo)
    
    def print_tree(self):
        if self.cargo is None: return 0
        print(self.cargo, end = ' ')
        self.left.print_tree()
        self.right.print_tree()

if __name__=="__main__":
    left = Tree(2)
    right = Tree(3)
    tree = Tree(1, left, right)
    tree.print_tree()
