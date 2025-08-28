import random

class Node:
    def __init__(self, value, next:"Node" = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head:"Node"):
        self.head = head

    def insert_tail(self, node):

        if self.head is None:
            self.head = node
            return True

        scroller = self.head
        while(scroller.next is not None):
            scroller = scroller.next

        scroller.next = node
        return True


class GenericTree:
    def __init__(self, parent, firstChild, value):
        self.parent = parent
        self.firstChild = firstChild
        self.value = value
     
        if parent is None:
            self.level = 0
        else:
            self.level = parent.level + 1

    def generateChild(self, value):
        child = GenericTree(self, None, value)

        if self.firstChild is None:
            self.firstChild = LinkedList(Node(child))
        else:
            self.firstChild.insert_tail(Node(child))
        
        return child


    # DFS preorder print
    def __str__(self):
        return self._to_string()

    def _to_string(self, indent: int = 0):
        # Current node line
        result = "  " * indent + str(self.value) + "\n"

        # Traverse children if any
        if self.firstChild:
            node = self.firstChild.head
            while node:
                result += node.value._to_string(indent + 1)
                node = node.next

        return result

if __name__ == "__main__":
    root = GenericTree(None, None, 'root')
    c1 = root.generateChild(1)
    c2 = root.generateChild(2)
    c1.generateChild(11)
    c1.generateChild(12)
    c2.generateChild(21)

    print(root)    