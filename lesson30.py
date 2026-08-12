# LESSON 30.1: LINKED LISTS

# Node	
# A self-contained object that acts as a single link in a linked list, 
# containing data and a reference to the next node.

# Pointer (next)	
# An attribute inside a node that stores the memory address of the next node in the sequence.

# Head	
# A reference pointer that tracks the first node in a linked list. 
# If the list is empty, the head is None.

# Traversal	The process of starting at the head node and 
# following the next pointers step-by-step to read or modify each item

# Broken Link (Memory Leak)	An error where a pointer is overwritten before its downstream connections are saved, 
# causing those objects to be lost in memory.


# Step-by-Step Implementation
# Step 1: Building the Node Class (CupNode)
# A linked list is built out of individual Nodes. In our coffee cart, we will define a CupNode class. It has two attributes inside its __init__ constructor:

# customer_name: The data we want to store (a string).
# next: The pointer link. It defaults to None because when a cup is first stamped out, it is not connected to anything yet.

# EXAMPLE 1
class CupNode:
    def __init__(self, name):
        self.customer_name = name  # The data stored in the link
        self.next = None           # Pointer to the next cup (defaults to empty)

node_1 = CupNode("David")
print(node_1.customer_name)
print(node_1.next)

# EXAMPLE 2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node_1 = Node("Alice")
print(node_1.data)
print(node_1.next)