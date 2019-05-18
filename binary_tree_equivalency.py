#!/usr/bin/env python3

class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def pre_order_traversal(node1, node2, level):
    print("LEVEL:", level)
    if node1 and node2:
        if node1.data != node2.data:
            print("node1 not equal to node2 in here - should return False")
            return False
        print("node1.data: " + str(node1.data))
        print("node2.data: " + str(node2.data))

        return pre_order_traversal(node1.left, node2.left, level + 1) and \
               pre_order_traversal(node1.right, node2.right, level + 1)
    elif not node1 and not node2:
        print("node1 and node2 are None here!")
        return True

    else:
        return False

def is_same_tree(node1, node2):
    if not node1 and not node2:
        return True
    else:
        return pre_order_traversal(node1, node2, 1)

# Empty trees
node1 = None
node2 = None
assert(is_same_tree(node1, node2))

# Single node equal trees
node1 = Node(1)
node2 = Node(1)
assert(is_same_tree(node1, node2))

# Single node NOT equal VALUE trees
node1 = Node(1)
node2 = Node(5)
assert(is_same_tree(node1, node2) == False)

# Single node NOT equal NODE COUNT trees
node1 = Node(1)
node1.left = Node(2)
node2 = Node(1)
assert(is_same_tree(node1, node2) == False)

# Small equal trees
node1 = Node(1)
node1.left = Node(2)
node1.right = Node(3)

node2 = Node(1)
node2.left = Node(2)
node2.right = Node(3)

assert(is_same_tree(node1, node2))

# Trees are equal
node1 = Node(1)
node1.left = Node(2)
node1.left.left = Node(3)
node1.right = Node(4)
node1.right.left = Node(5)
node1.right.right = Node(6)

node2 = Node(1)
node2.left = Node(2)
node2.left.left = Node(3)
node2.right = Node(4)
node2.right.left = Node(5)
node2.right.right = Node(6)

assert(is_same_tree(node1, node2))

# Trees are NOT equal
node1 = Node(1)
node1.left = Node(2)
node1.left.left = Node(3)
node1.right = Node(4)
node1.right.left = Node(5)
node1.right.right = Node(6)

node2 = Node(1)
node2.left = Node(2)
node2.left.left = Node(9)
node2.right = Node(4)
node2.right.left = Node(5)
node2.right.right = Node(6)

assert(is_same_tree(node1, node2) == False)
