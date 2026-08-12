<<<<<<< HEAD
=======
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
>>>>>>> 341ec26982516ed1036b1c93ff1a61f71a35ead1
class CupNode:
    def __init__(self, name):
        self.customer_name = name  # The data stored in the link
        self.next = None           # Pointer to the next cup (defaults to empty)
<<<<<<< HEAD
cup_1 = CupNode("David")
print(cup_1.customer_name)
print(cup_1.next)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node_1 = Node("Alice")
print(node_1.data)
print(node_1.next)

# Step 2: Manually Linking Nodes
# 1. Create three separate cup nodes
cup_1 = CupNode("Alice")
cup_2 = CupNode("Bob")
cup_3 = CupNode("Charlie")

# 2. Tie the strings!
cup_1.next = cup_2  # Alice points to Bob
cup_2.next = cup_3  # Bob points to Charlie
# cup_3.next remains None (the end of the line)

# 3. Read the linked chain using nested dot notation
print(cup_1.next.customer_name)       # Output: Bob
print(cup_1.next.next.customer_name)  # Output: Charlie

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

n1 = Node("A")
n2 = Node("B")
n1.next = n2

print(n1.next.val)


# Step 3: Building the Linked List Manager Class (CupChain)
# Manually linking nodes using nested .next.next is impractical. We need a manager class called CupChain to control the chain. This class only needs to track one state variable: self.head (the red flag pointing to the first node).

# We will write an append(name) method inside this class to automatically walk to the end of the chain and tie a new cup there.

class CupChain:
    def __init__(self):
        self.head = None  # The chain starts empty (no red flag on the counter)
        
    def append(self, name):
        new_cup = CupNode(name)
        
        # Scenario A: If the chain is empty, make this cup the head
        if self.head is None:
            self.head = new_cup
            return
            
      # Scenario B: Walk to the end of the chain and tie the new cup there
        current = self.head
        while current.next is not None:
            current = current.next  # Follow the string to the next cup
            
        current.next = new_cup  # Tie the new cup to the last cup's empty hook



# Step 4: Traversing the Chain
# To print all customer names currently waiting in the chain, we use a loop pattern called Traversal. We start a temporary pointer variable current at self.head, and walk down the chain using a while loop that runs as long as current is not None.

# Let us track the state transitions as we traverse a chain containing Alice, Bob, and Charlie.

class CupChain:
    def __init__(self):
        self.head = None  # The chain starts empty (no red flag on the counter)
        
    def append(self, name):
        new_cup = CupNode(name)
        
        # Scenario A: If the chain is empty, make this cup the head
        if self.head is None:
            self.head = new_cup
            return
            
      # Scenario B: Walk to the end of the chain and tie the new cup there
        current = self.head
        while current.next is not None:
            current = current.next  # Follow the string to the next cup
            
        current.next = new_cup  # Tie the new cup to the last cup's empty hook


    def traverse_and_print(self):
        current = self.head  # Start at the red "HEAD" flag
        
        while current is not None:
            print(f"Customer Cup: {current.customer_name}")
            current = current.next  # Move our hand to the next cup in line

# Instantiate and run
my_chain = CupChain()
my_chain.append("Alice")
my_chain.append("Bob")
my_chain.traverse_and_print()

=======

node_1 = CupNode("David")
print(node_1.customer_name)
print(node_1.next)

>>>>>>> 341ec26982516ed1036b1c93ff1a61f71a35ead1
# EXAMPLE 2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

<<<<<<< HEAD
head = Node("Start")
head.next = Node("End")

current = head
while current is not None:
    print(current.data)
    current = current.next
=======
node_1 = Node("Alice")
print(node_1.data)
print(node_1.next)
>>>>>>> 341ec26982516ed1036b1c93ff1a61f71a35ead1
