# %%
import collections


class Node:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children if children else []

    def add_child(self, child):
        self.children.append(child)


class Tree:
    def __init__(self, root_node):
        self.root = root_node

    def traverse_bf(self):
        queue = collections.deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            print(node.data)
            queue.extend(node.children)

    def traverse_df(self):
        def df(node):
            print(node.data)
            for child_node in node.children:
                df(child_node)

        df(self.root)


t = Tree(Node("a"))
t.root.add_child(Node("b"))
t.root.add_child(Node("c"))
t.root.add_child(Node("d"))
t.root.children[0].add_child(Node("e"))
t.root.children[1].add_child(Node("f"))
t.root.children[1].add_child(Node("g"))
t.root.children[2].add_child(Node("h"))

t.traverse_bf()
print("---")
t.traverse_df()
