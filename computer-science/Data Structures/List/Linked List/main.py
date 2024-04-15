# %%
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self, elements: list = []):
        self.head = None
        for el in reversed(elements):
            self.insert_at_beginning(el)

    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def remove_from_beginning(self):
        self.head = self.head.next

    def insert_at_end(self, data):
        new_node = Node(data)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node

    def remove_from_end(self):
        itr = self.head

        while itr:
            if itr.next.next is None:
                itr.next = None
                break
            itr = itr.next

    def traverse_print(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next

    def traverse_print_recursively(self, curr=None):
        if curr is None:
            curr = self.head
        print(curr.data)
        if curr.next is not None:
            self.traverse_print_recursively(curr.next)


# %%
ll = SinglyLinkedList()

ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)

ll.insert_at_end(4)
ll.remove_from_end()

ll.traverse_print()
ll.traverse_print_recursively()


# %%
def reverse(ll: SinglyLinkedList) -> SinglyLinkedList:
    reversed_list = SinglyLinkedList()
    curr = ll.head
    while curr:
        reversed_list.insert_at_beginning(curr.data)
        curr = curr.next
    return reversed_list


ll = SinglyLinkedList([1, 2, 3])
reverse(ll).traverse_print()


# %%
def reverse_in_place(ll: SinglyLinkedList) -> SinglyLinkedList:
    # Time: O(n)
    # Space: O(1)
    curr = ll.head
    prev = None  # the previous item has to be remembered because on a linked list you can't access the previous element

    while curr:
        # stash the next element so that we can traverse the original list
        next = curr.next

        # switch the pointer direction
        curr.next = prev
        prev = curr

        # jump to the next element in the original list
        curr = next

    ll.head = prev


ll = SinglyLinkedList([1, 2, 3, 4, 5])
reverse_in_place(ll)
ll.traverse_print()


# %%
def reverse_in_place_recursively(ll: SinglyLinkedList, prev=None) -> SinglyLinkedList:
    # Time: O(n)
    # Space: O(n) due to the callstack

    curr = ll.head

    next = curr.next

    curr.next = prev
    prev = curr

    # base case
    if next:
        ll.head = next
        reverse_in_place_recursively(ll, prev)
    else:
        curr = prev


ll = SinglyLinkedList([1, 2, 3, 4, 5])
reverse_in_place_recursively(ll)
ll.traverse_print()


# %%
def reversed_list_head(head: Node) -> Node:
    if head is None or head.next is None:
        return head

    rest_reversed = reversed_list_head(head.next)
    head.next.next = head  # modify the tail of the rest_reversed
    head.next = None  # point the new tail of the rest_reversed to null because we don't know yet if it is the last one
    return rest_reversed


def reverse_in_place_recursively2(ll: SinglyLinkedList):
    ll.head = reversed_list_head(ll.head)
    return ll.head


ll = SinglyLinkedList([1, 2, 3, 4, 5])
reverse_in_place_recursively2(ll)
ll.traverse_print()
