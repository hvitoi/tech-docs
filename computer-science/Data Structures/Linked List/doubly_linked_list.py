# %%
class Node:
    def __init__(self, data, *, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, elements: list = None):
        self.head = None
        self.tail = None

        if elements is None:
            elements = []

        for el in elements:
            self.push_right(el)

    def push_left(self, data):
        new_node = Node(data, next=self.head)
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def pop_left(self):
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def push_right(self, data):
        new_node = Node(data, prev=self.tail)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node

    def pop_right(self):
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None

    def traverse_from_left(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next

    def traverse_from_right(self):
        itr = self.tail
        while itr:
            print(itr.data)
            itr = itr.prev


ll = DoublyLinkedList()

ll.push_left("c")
ll.push_left("b")
ll.push_left("a")

ll.push_right("x")
ll.push_right("y")
ll.push_right("z")

ll.pop_left()
ll.pop_right()

ll.traverse_from_left()
ll.traverse_from_right()
