from lists import MyList

class genericTree():
    def __init__(self, parent, value, children,level=0):
        self.parent = parent
        self.value = value
        self.children = children
        self.level = level

    # FIXME - fix this fucking method and MyList.insert_head method
    def generateChild(self, value):
        child = genericTree(self, value, MyList(), self.level + 1)
        self.children.insert_head(child)

    def getChildren(self):
        return self.children
    
    def __str__(self):
        def build_str(node, indent=""):
            # Print the current node value
            result = f"{indent}{node.value}\n"
            # Iterate children
            child_list = node.children
            while child_list is not None and not child_list.is_empty():
                child_node = child_list.value  # genericTree
                result += build_str(child_node, indent + "  ")
                child_list = child_list.next
            return result

        return build_str(self).rstrip()

def test_generic_tree():
    print("=== TEST genericTree ===")

    # Create root node
    root = genericTree(None, 1, MyList())
    print("Root value:", root.value)   # 1
    print("Root parent:", root.parent) # None
    print(root)

    # Add first child
    root.generateChild(2)
    print("\nAfter adding child 2:")
    print(root)

    # Add second child
    root.generateChild(3)
    print("\nAfter adding child 3:")
    print(root)

    root.generateChild(4)
    print("\nAfter adding child 4:")
    print(root)


    # # Add child to node 2
    # child2 = root.getChildren().value  # this is node with value=2 (since inserted at head last)
    # child2.generateChild(4)
    # child2.generateChild(5)
    # print("\nAfter adding children 4 and 5 to node 2:")
    # print(root)

    # # Add child to node 3
    # child3 = root.getChildren().next.value  # node with value=3
    # child3.generateChild(6)
    # print("\nAfter adding child 6 to node 3:")
    # print(root)

    # # Traversal check
    # print("\nChildren of root (should be 3 and 2):")
    # children = root.getChildren()
    # while children is not None and not children.is_empty():
    #     print(children.value.value, end=" ")
    #     children = children.next
    # print("\n")

# Run tests
if __name__ == "__main__":
    test_generic_tree()