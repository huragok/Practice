#! /usr/bin/env python3

import unittest
import TreeBinary as tb
import random

class TestTreeBinary(unittest.TestCase):
    def setUp(self):
        self.tree = tb.TreeBinary()
        
        self.keys = [12, 5, 18, 2, 9, 15, 19, 13, 17]
        for key in self.keys:
            self.tree.insert(tb.Node(key))  
             
    def test_search(self):
        self.assertEqual(12, self.tree.search(12).key)
        self.assertEqual(None, self.tree.search(7))

    def test_min_max(self):
        self.assertEqual(min(self.keys), self.tree.min.key)
        self.assertEqual(max(self.keys), self.tree.max.key)        


    def test_predecessor(self):
        node_1 = self.tree.search(13)
        self.assertEqual(12, self.tree.predecessor(node_1).key)
        node_2 = self.tree.search(2)
        self.assertEqual(None, self.tree.predecessor(node_2))
        node_3 = self.tree.search(12)
        self.assertEqual(9, self.tree.predecessor(node_3).key)

    def test_successor(self):
        node_1 = self.tree.search(9)
        node_2 = self.tree.search(19)
        node_3 = self.tree.search(12)
        
        self.assertEqual(12, self.tree.successor(node_1).key) 
        self.assertEqual(None, self.tree.successor(node_2))
        self.assertEqual(13, self.tree.successor(node_3).key)
    def test_insert_walk(self):
        self.assertEqual(sorted(self.keys), self.tree.walk_in_order())
    
    def test_delete(self):
        node_1 = self.tree.search(2)
        node_2 = self.tree.search(18)
        self.tree.delete(node_1)
        self.keys.remove(2)
        self.assertEqual(sorted(self.keys), self.tree.walk_in_order())
        self.tree.delete(node_2)
        self.keys.remove(18)
        self.assertEqual(sorted(self.keys), self.tree.walk_in_order())
          

if __name__ == "__main__":
    unittest.main()
