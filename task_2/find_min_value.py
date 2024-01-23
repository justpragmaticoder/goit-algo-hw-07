from avl_tree import AVLNode
from binary_tree import Node


def find_min_node_value(node):
    if node is None or ((not (isinstance(node, AVLNode) or isinstance(node, Node)))):
        return None

    current = node
    while current.left is not None:
        current = current.left

    if hasattr(node, "key"):
        return current.key
    elif hasattr(node, "val"):
        return current.val

    return None
