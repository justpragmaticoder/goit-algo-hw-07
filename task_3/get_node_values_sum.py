from avl_tree import AVLNode
from binary_tree import Node


def get_node_values_sum(node):
    current_value = 0

    if node is None or ((not (isinstance(node, AVLNode) or isinstance(node, Node)))):
        return current_value

    if hasattr(node, "key"):
        current_value = node.key
    elif hasattr(node, "val"):
        current_value = node.val

    return (
        current_value + get_node_values_sum(node.left) + get_node_values_sum(node.right)
    )
