#! /usr/bin/env python3

import list_custom_sort as lcs
import unittest
import random

class TestSort(unittest.TestCase):
    def setUp(self):
        self.unsorted = lcs.list_custom_sort([2, 4, 5, 7, 1, 2, 3, 6])
        self.original = self.unsorted[:]

    def test_sort_insert(self):
        self.unsorted.sort_insert()
        self.assertEqual(self.unsorted, sorted(self.original))

    def test_sort_merge(self):
        self.unsorted.sort_merge()
        self.assertEqual(self.unsorted, sorted(self.original))
        
if __name__ == "__main__":
    unittest.main()
