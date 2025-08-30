# class MyList:
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next

#     def is_empty(self):
#         return self.value is None and self.next is None

#     def insert_head(self, node):
#         self.value, node.value = node.value, self.value


#         node.next = self.next
#         self.next = node

#     def insert_position(self, node, index):
#         tmp = self.search(index-1)

#         node.next = tmp.next
#         tmp.next = node

#     def insert_last(self, node):
#         if self.value == None:
#             self.value = node.value
#             self.next = node.next
        
#         else:

#             tmp = self

#             while (tmp.next is not None):
#                 tmp = tmp.next

#             tmp.next = node

#     def delete(self, value):
#         if self.value == value:
#             if self.next is None:  
#                 # Only one node in list
#                 self.value = None
#             else:
#                 # Copy data from next node into current
#                 self.value = self.next.value
#                 self.next = self.next.next
#             return True

#         # Case 2: deleting non-head node
#         prev = self
#         curr = self.next

#         while curr is not None:
#             if curr.value == value:
#                 prev.next = curr.next
#                 return True
#             prev, curr = curr, curr.next

#         # Value not found
#         return False

#     def search(self, index):
#         tmp = self
#         for i in range(index):
#             tmp = tmp.next
#             if tmp is None:
#                 print('index not found')
#                 return None
            
        
#         return tmp

#     @staticmethod
#     def insert_next(previous_node, next_node):
#         next_node.next = previous_node.next
#         previous_node.next = next_node



#     def __str__(self):
#         def build_str(self):
#             if self ==  None:
#                 return 'None'
#             else:
#                 return f'{self.value} -> {build_str(self.next)}'
            
    
#         return build_str(self)


from typing import TypeVar, Generic, Optional

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, value: T, next: Optional["Node[T]"] = None):
        self.value: T = value
        self.next: Optional[Node[T]] = next

    def __repr__(self) -> str:
        return f"Node({self.value})"


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None

    def is_empty(self) -> bool:
        return self.head is None

    def insert_head(self, value: T) -> None:
        self.head = Node(value, self.head)

    def insert_tail(self, value: T) -> None:
        if self.head is None:
            self.head = Node(value)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(value)

    def delete(self, value: T) -> bool:
        if self.head is None:
            return False

        # Delete head
        if self.head.value == value:
            self.head = self.head.next
            return True

        prev, curr = self.head, self.head.next
        while curr:
            if curr.value == value:
                prev.next = curr.next
                return True
            prev, curr = curr, curr.next
        return False

    def search(self, value: T) -> Optional[Node[T]]:
        curr = self.head
        while curr:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    def __str__(self) -> str:
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.value))
            curr = curr.next
        return " -> ".join(values) + " -> None"
