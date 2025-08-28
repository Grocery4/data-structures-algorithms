import random

from lists import Node, LinkedList

class GenericTree:
    def __init__(self, parent, children, value):
        self.parent = parent
        self.children = children
        self.value = value
     
        if parent is None:
            self.level = 0
        else:
            self.level = parent.level + 1

    def generateChild(self, value) -> "GenericTree":
        child = GenericTree(self, LinkedList[GenericTree](), value)
        self.children.insert_tail(child)
        return child

    # DFS preorder print
    def __str__(self) -> str:
        def recurse(node: "GenericTree", indent: int = 0) -> str:
            spaces = "  " * indent
            s = f"{spaces}Node({node.value})\n"
            curr = node.children.head
            while curr:
                s += recurse(curr.value, indent + 1)
                curr = curr.next
            return s
        return recurse(self)

    # DFS postorder print    
    # def __str__(self) -> str:
    #     def recurse(node: "GenericTree", indent: int = 0) -> str:
    #         spaces = "  " * indent
    #         s = ""
    #         curr = node.children.head
    #         while curr:
    #             s += recurse(curr.value, indent + 1)
    #             curr = curr.next
    #         s += f"{spaces}Node({node.value})\n"
    #         return s
    #     return recurse(self)

    
def generate_random_generic_tree(num_nodes: int) -> GenericTree:
    root = GenericTree(None, LinkedList[GenericTree](), "root")
    nodes = [root]
    for i in range(1, num_nodes):
        # Randomly select a parent from existing nodes
        parent = random.choice(nodes)
        child = parent.generateChild(f"node_{i}")
        nodes.append(child)
    return root

if __name__ == "__main__":
    tree = generate_random_generic_tree(21)
    print(tree)