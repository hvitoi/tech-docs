# %%


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        node = self.root

        if node is None:
            self.root = new_node
            return

        while True:
            if data > node.data:
                if node.right is None:
                    node.right = new_node
                    break
                else:
                    node = node.right
                    continue
            elif data < node.data:
                if node.left is None:
                    node.left = new_node
                    break
                else:
                    node = node.left
                    continue

    def insert_recursively(self, data, *, root=None):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        node = root if root is not None else self.root

        if data > node.data:
            if node.right is None:
                node.right = new_node
                return
            else:
                self.insert_recursively(data, root=node.right)
                return
        elif data < node.data:
            if node.left is None:
                node.left = new_node
                return
            else:
                self.insert_recursively(data, root=node.left)
                return
        else:
            raise Exception("Duplicated value")

    def lookup(self, target, *, root=None) -> bool:
        node = root if root is not None else self.root

        if not isinstance(node, Node):
            return False

        if target == node.data:
            return True

        if target > node.data and isinstance(node.right, Node):
            return self.lookup(target, root=node.right)

        if target < node.data and isinstance(node.left, Node):
            return self.lookup(target, root=node.left)

        return False


# %%
bst = BST()
bst.insert(5)
bst.insert(15)
bst.insert(0)
bst.insert(20)

# %%
bst = BST()
bst.insert_recursively(5)
bst.insert_recursively(15)
bst.insert_recursively(0)
bst.insert_recursively(20)

# %%
bst = BST()
bst.insert(5)
bst.insert(15)
bst.insert(0)
bst.insert(20)

bst.lookup(5)  # True
bst.lookup(99)  # False
