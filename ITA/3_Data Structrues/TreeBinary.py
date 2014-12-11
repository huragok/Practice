#! /usr/bin/env python3

class Node:
    def __init__(self, key = 0):
        self.p = None
        self.left = None
        self.right = None
        self.key = key

class TreeBinary:
    def __init__(self):
        self.root = None
    
    @property
    def max(self):
        pass

    @property
    def min(self):
        pass

    def successor(self, key):
        pass

    def predecessor(self, key):
        pass

    def insert(self, node):
        node_prev = self.root
        node_cur = self.root
        while node_cur is not None:
            node_prev = node_cur
            if node_cur.key < node.key:
                node_cur = node_cur.right
            else:
                node_cur = node_cur.left
        node.p = node_prev
        if node_prev is None:
            self.root = node
        elif node_prev.key < node.key:
            node_prev.right = node
        else:
            node_prev.left = node

    def delete(self, key):
        pass

    def walk_in_order(self):
        def walk_in_order_from(node):
            while node is not None:
                keys_ordered_left = walk_in_order_from(node.left)
                keys_ordered_right = walk_in_order_from(node.right)
                return keys_ordered_left + [node.key] + keys_ordered_right
            return []

        keys_ordered = walk_in_order_from(self.root)
        return keys_ordered
