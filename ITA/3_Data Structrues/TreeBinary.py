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
    
    def search(self, key):
        node_cur = self.root
        while node_cur is not None:
            if key < node_cur.key:
                node_cur = node_cur.left
            elif key > node_cur.key:
                node_cur = node_cur.right
            else:
                break
        return node_cur
         
    @property
    def max(self):
        if self.root is None:
            return None
        node_cur = self.root
        while node_cur.right is not None:
            node_cur = node_cur.right
        return node_cur

    @property
    def min(self):
        if self.root is None:
            return None
        node_cur = self.root
        while node_cur.left is not None:
            node_cur = node_cur.left
        return node_cur
         

    def successor(self, node): # should have been implemented as property of node object
        if node is None:
            return None
        if node.right is not None:
            tree_tmp = TreeBinary()
            tree_tmp.root = node.right
            return tree_tmp.min
        node_cur = node
        while node_cur.p is not None and node_cur.p.right == node_cur:
            node_cur = node_cur.p
        return node_cur.p 

    def predecessor(self, node):
         
        node_cur = node
        if node_cur is None:
            return node_cur
        
        if node_cur.left is not None:
            tree_tmp = TreeBinary()
            tree_tmp.root = node_cur.left
            return tree_tmp.max
        while node_cur.p is not None and node_cur == node_cur.p.left:
            node_cur = node_cur.p
        return node_cur.p

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
    
    def transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def delete(self, node):
        if node is None:
            return
        
        if (node.left, node.right) == (None, None):
            self.transplant(node, None)
        elif node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            node_suc = self.successor(node)
            if node_suc is not node.right: # not direct right child
                self.transplant(node_suc.right, node)
                node_suc.right = node.right
                node_right.p = node_suc
            self.transplant(node, node_suc)
            node_suc.left = node.left
            node.left.p = node_suc
        

    def walk_in_order(self):
        def walk_in_order_from(node):
            while node is not None:
                keys_ordered_left = walk_in_order_from(node.left)
                keys_ordered_right = walk_in_order_from(node.right)
                return keys_ordered_left + [node.key] + keys_ordered_right
            return []

        keys_ordered = walk_in_order_from(self.root)
        return keys_ordered
