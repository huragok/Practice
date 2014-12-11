#! /usr/bin/env python3

import unittest
import TreeBinary as tb
import random

class TestTreeBinary(unittest.TestCase):
    def setUp(self):
        self.tree = tb.TreeBinary()

    def test_search(self):
        pass

    def test_min(self):
        pass

    def test_max(self):
        pass

    def test_predecessor(self):
        pass

    def test_successor(self):
        pass

    def test_insert_walk(self):
        keys = (12, 5, 18, 2, 9, 15, 19, 13, 17)
        for key in keys:
            self.tree.insert(tb.Node(key))   
        self.assertEqual(sorted(keys), self.tree.walk_in_order())
    
    def test_delete(self):
        pass

if __name__ == "__main__":
    unittest.main()
