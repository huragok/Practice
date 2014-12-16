#! /usr/bin/env python3
t = 3;

class BTreeNode:
    def __init__(self): # t determinse the branch factor
        self.keys = [] # Keys, [t - 1, 2t -1] if not root
        self.childrens = [] # Childrens, [t, 2t] if not root nor leaf
        self.n = 0 # Number of keys
        self.leaf = False # Whether leaf or not

    def split_child(self, i): # Split the full child self.childrens[i]
        child_new = BTreeNode() # The new right siblings to self.childrens[i]
        child_new.leaf = self.childrens[i].leaf
        child_new.n = t - 1
        child_new.keys = self.childrens[i].keys[t : ]
        if child_new.leaf == False: # Copy the childrens
            child_new.childrens = self.childrens[i].childrens[t :]
            
        self.childrens[i].n = t - 1
        self.childrens[i].keys = self.childrens[i].keys[0 : t - 1]
        if self.childrens[i].leaf == False:
            self.childrens[i].childrens = self.childrens[i].childrens[0 : t]

        # Now insert the middle of self.children[i]'s keys into self.keys



    def insert_nonfull(self, k): # self is not full, insert key into the sub B tree from self
        if self.leaf == True: # If is a nonfull leaf node, insert into its keys
            i = 0 # Indices to insert this key
            while self.keys[i] < k and i < n:
                i += 1
            self.keys = self.keys[0 : i] + [k] + self.keys[i : ]
            self.n += 1
        else: # If is a nonfull internal node, split the children corresponding to the key
            i = 0 # The children to split
            while self.keys[i] < k and i < n:
                i += 1
            if self.childrens[i].n == 2 * t - 1: # In case this child is full
                self.split_child(i) # Split the i-th child into the i-th and the i+1-th child
                if k > self.keys[i]:
                    i += 1

            self.childrens[i].insert_nonnull(k)


    def delete(self, k): # Delete key k from the sub B tree starting from self 
        pass

class BTree:
    def __init__(self):
        self.root = BTreeNode()
        self.root.leaf = True
    
    def search(self, k): # Search for key k in the tree
        pass

    def insert(self, k): # Insert key k from the root in a top down one pass manner
        node = self.root
        if node.n == 2 * t - 1: # root node is full, we need to get a new root above it and split the current one
            root_new = BTReeNode()
            root_new.childrens = [node]
            self.root = root_new
            root_new.split_child(0) # Its only child [0] is full, split it
            root_new.insert_nonfull(k)
        else:
            node.insert_nonfull(k) # root is not full, directly insert from it
                            

    def delete(self, k): # Delete key k from the root in a top down one pass manner
        pass

def main():
    pass

if __name__ == "__main__":
    main()
