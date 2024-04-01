# %%


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, elements: list = []):
        self.head = None
        for el in reversed(elements):
            self.insert_at_beginning(el)

    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node

    def print(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next


ll = LinkedList()

ll.insert_at_beginning("red")
ll.insert_at_beginning("green")
ll.insert_at_beginning("blue")

ll.insert_at_end("yellow")

ll.print()

# %%

ll = LinkedList([1, 2, 3])
ll.print()
