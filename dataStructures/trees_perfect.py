class PerfectTree:
    def __init__(self, parent=None, left=None, right=None, value=None, level=0):
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value
        self.level = level

    def generateChild(self, parent, value, new_level):
        return PerfectTree(parent, None, None, value, new_level)
    
    # both methods override previous values.
    def generateLeft(self, value):
        self.left = self.generateChild(self, value, self.level)
        self.level+=1
    def generateRight(self, value):
        self.right = self.generateChild(self, value, self.level)
        self.level+=1

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def nodeCounter(self):
        if self.left == None and self.right == None:
            return 1

        # 1 is root node
        count = 1 + self.getLeft().nodeCounter() + self.getRight().nodeCounter()

        return count

    def __str__(self):
        return self._build_str()

    def _build_str(self, prefix="", is_left=True):
        result = ""
        if self.right is not None:
            result += self.right._build_str(prefix + ("│   " if is_left else "    "), False)

        result += prefix + ("└── " if is_left else "┌── ") + str(self.value) + "\n"

        if self.left is not None:
            result += self.left._build_str(prefix + ("    " if is_left else "│   "), True)

        return result
    
    def __repr__(self):
        return self._build_repr()
        
    def _build_repr(self, indent=0):
        result = " " * indent + str(self.value) + "\n"

        if self.left is not None:
            result += self.left._build_repr(indent + 4)

        if self.right is not None:
            result += self.right._build_repr(indent + 4)

        return result

    def __lt__(self, other):
        return self.value < other.value
    

def generate_perfect_binary_tree(current, depth):
    if depth <= 1:
        return
    current.left = PerfectTree(current, None, None, current.value * 2, current.level + 1)
    current.right = PerfectTree(current, None, None, current.value * 2 + 1, current.level + 1)
    generate_perfect_binary_tree(current.left, depth - 1)
    generate_perfect_binary_tree(current.right, depth - 1)

if __name__ == "__main__":
    root = PerfectTree(None, None, None, 1)
    generate_perfect_binary_tree(root, 5)
    print(root)
    print('total nodes:', root.nodeCounter())