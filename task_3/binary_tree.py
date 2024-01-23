class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert_binary_tree_node(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert_binary_tree_node(root.left, key)
        else:
            root.right = insert_binary_tree_node(root.right, key)
    return root
