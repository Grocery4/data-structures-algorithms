class MyList:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def is_empty(self):
        return self.value == None

    def insert_head(self, node):
        MyList.insert_next(self,node)
        self.value, node.value = node.value, self.value

    def getValue(self):
        return self.value
    
    @staticmethod
    def create_list(value=None):
        return MyList(value)

    @staticmethod
    def insert_next(previous, insert):
        insert.next = previous.next
        previous.next = insert

    @staticmethod
    def insert_position(lst, node, index):
        tmp = lst
        for i in range(index):
            tmp = tmp.next
        
        MyList.insert_next(tmp, node)

    @staticmethod
    def search(lst, index):
        tmp = lst
        for i in range(index):
            if tmp == None:
                print('not found.')
                return

            tmp = tmp.next

        return tmp

    @staticmethod
    def delete_from_list(lst, node):
        tmp = lst
        while(tmp is not None and tmp.next is not None):
            if tmp.next.value == node.value:
                tmp.next = tmp.next.next
                return
            
            tmp = tmp.next

    def __str__(self):
        values = []
        tmp = self
        while tmp is not None and not tmp.is_empty():
            values.append(str(tmp.value))
            tmp = tmp.next
        return " -> ".join(values) + " -> None"



def test_mylist():
    print("=== TEST create_list ===")
    l = MyList.create_list(10)
    print(l.getValue() == 10)   # True
    
    print("=== TEST is_empty ===")
    empty = MyList()
    print(empty.is_empty())     # True
    print(l.is_empty())         # False

    print("=== TEST insert_head ===")
    head = MyList(5)
    head = head.insert_head(MyList(1))  # insert before 5
    print(head.getValue() == 1)         # True
    print(head.next.getValue() == 5)    # True

    print("=== TEST insert_next ===")
    a = MyList(1)
    b = MyList(2)
    c = MyList(3)
    MyList.insert_next(a, b)   # insert b after a
    MyList.insert_next(b, c)   # insert c after b
    print(a.getValue(), a.next.getValue(), a.next.next.getValue())  # 1,2,3

    print("=== TEST insert_position ===")
    l = MyList(0)
    l.next = MyList(2)
    MyList.insert_position(l, MyList(1), 0)  # insert after index 0
    print(l.getValue(), l.next.getValue(), l.next.next.getValue())  # 0,1,2

    print("==== TEST search ====")
    head = MyList(10)
    node2 = MyList(20)
    node3 = MyList(30)
    head.next = node2
    node2.next = node3

    print("Testing search on list: 10 -> 20 -> 30 -> None")

    # Search index 0 (should return head with value=10)
    found = MyList.search(head, 0)
    print("Index 0:", found.value if found else None)

    # Search index 1 (should return node2 with value=20)
    found = MyList.search(head, 1)
    print("Index 1:", found.value if found else None)

    # Search index 2 (should return node3 with value=30)
    found = MyList.search(head, 2)
    print("Index 2:", found.value if found else None)

    # Search index 5 (out of range, should print 'not found.')
    found = MyList.search(head, 5)
    print("Index 5:", found.value if found else None)

    print("==== TEST delete_from_list ====")
    head = MyList(1)
    node2 = MyList(2)
    node3 = MyList(3)
    head.next = node2
    node2.next = node3

    print("Original list:")
    tmp = head
    while tmp:
        print(tmp.value, end=" -> ")
        tmp = tmp.next
    print("None")

    # delete node2 (value=2)
    MyList.delete_from_list(head, node2)

    print("After deleting node with value=2:")
    tmp = head
    while tmp:
        print(tmp.value, end=" -> ")
        tmp = tmp.next
    print("None")

    # delete node3 (value=3)
    MyList.delete_from_list(head, node3)

    print("After deleting node with value=3:")
    tmp = head
    while tmp:
        print(tmp.value, end=" -> ")
        tmp = tmp.next
    print("None")

if __name__ == '__main__':
    # test_mylist()
    a = MyList()
    a.insert_head(MyList(2))
    a.insert_head(MyList(5))
    print(a)