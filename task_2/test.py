import unittest
from avl_tree import insert_avl_node
from binary_tree import insert_binary_tree_node
from find_min_value import find_min_node_value


class Test(unittest.TestCase):
    def test_find_min_value_in_avl(self):
        root = None
        keys = [20, 30, 25, 28, 27, -1, 128, 256, 931]

        for key in keys:
            root = insert_avl_node(root, key)

        max_value = find_min_node_value(root)

        self.assertEqual(max_value, -1)

    def test_find_min_value_in_binary_tree(self):
        root = None
        keys = [3, 2, 4, 7, 6, 8, 120, 77, 55, 321]

        for key in keys:
            root = insert_binary_tree_node(root, key)

        max_value = find_min_node_value(root)

        self.assertEqual(max_value, 2)
