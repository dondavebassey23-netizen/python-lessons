# LESSON 31.1: BINARY SEARCH TREES

# Step-by-Step Implementation
# Step 1: Building the Node Class (CupNode)
# A Binary Search Tree is built out of individual nodes. In our coffee cart, we will define a CupNode class. It has three attributes inside its __init__ constructor:

# price: The key value we use for sorting (a float).
# left: A pointer link to a smaller child node (defaults to None).
# right: A pointer link to a larger child node (defaults to None).

# Example 1

class CupNode:
    def __init__(self, price):
        self.price = price  # The key value used for sorting
        self.left = None    # Pointer to smaller cup node
        self.right = None   # Pointer to larger cup node

node_root = CupNode(4.54)
print(node_root.price)
print(node_root.left)
print(node_root.right)

# Exampl 2

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

key_node = Node(59.00)
print(key_node.key)
print(key_node.left)

# Step 2: Inserting a Cup (The Sorting Rule)
# To insert a new cup into the tree, we write a recursive function. 
# This function compares the new price to the current node's price, and decides whether to branch left or right.


class CupNode:
    def __init__(self, price):
        self.price = price  # The key value used for sorting
        self.left = None    # Pointer to smaller cup node
        self.right = None   # Pointer to larger cup node

def insert(node, price):
    # Base Case: If we reach an empty spot, stamp out a new node here!
    if node is None:
        return CupNode(price)
        
    # Recursive Case: Decide which branch to follow
    if price < node.price:
        # If the new price is cheaper, go left
        node.left = insert(node.left, price)
    elif price > node.price:
        # If the new price is more expensive, go right
        node.right = insert(node.right, price)
        
    return node  # Return the unchanged node pointer

root = CupNode(4.00)
insert(root, 3.00)
insert(root, 5.00)

print(root.left.price)
print(root.right.price)

# Step 3: Searching the Tree
# To find a cup by its price tag, we write a recursive search function. 
# This function compares our target price to the current node:

# If they are equal, we found it!
# If the target is smaller, we search the left sub-tree.
# If the target is larger, we search the right sub-tree.

# Tree State:
# root = CupNode(4.00) -> left: CupNode(3.00), right: CupNode(5.00)

# THE COMPLETE CODE 

class CupNode:
    def __init__(self, price):
        self.price = price  # The key value used for sorting
        self.left = None    # Pointer to smaller cup node
        self.right = None   # Pointer to larger cup node

def insert(node, price):
    # Base Case: If we reach an empty spot, stamp out a new node here!
    if node is None:
        return CupNode(price)
        
    # Recursive Case: Decide which branch to follow
    if price < node.price:
        # If the new price is cheaper, go left
        node.left = insert(node.left, price)
    elif price > node.price:
        # If the new price is more expensive, go right
        node.right = insert(node.right, price)
        
    return node  # Return the unchanged node pointer



def search(node, target):
    # Base Cases: we reached the end of the tree, or we found the match!
    if node is None or node.price == target:
        return node
        
    # Recursive Cases: branch left or right
    if target < node.price:
        return search(node.left, target)
    else:
        return search(node.right, target)

# Build the tree

root = CupNode(4.00)
insert(root, 3.00)
insert(root, 5.00)

# Set the target and search
result_node = None
target_price = 5.00
result_node = search(root, target_price)
print(result_node.price)



# EXAMLE 3

root = CupNode(4.00)
insert(root, 3.00)
insert(root, 5.00)

found = search(root, 5.00)
print(found.price)
missing = search(root, 6.00)
print(missing)
