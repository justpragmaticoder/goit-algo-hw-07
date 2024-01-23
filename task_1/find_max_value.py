from avl_tree import AVLNode
from binary_tree import Node


def find_max_node_value(node):
    if node is None or ((not (isinstance(node, AVLNode) or isinstance(node, Node)))):
        return None

    current_node = node
    while current_node.right is not None:
        current_node = current_node.right

    if hasattr(node, "key"):
        return current_node.key
    elif hasattr(node, "val"):
        return current_node.val

    return None
