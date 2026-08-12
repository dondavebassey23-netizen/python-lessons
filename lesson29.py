# LESSON 29.1: STACKS AND QUEUES (WITH OOP)

# Step 1: The Vertical Cup Dispenser (Stack / LIFO)
# A Stack operates on the Last In, First Out (LIFO) principle. We implement a stack by wrapping a list inside a class and writing two primary methods:

# push(item): Adds an item to the end of our list using .append().
# pop(): Removes the last item from our list using .pop().

class CardboardCup:
    def __init__(self, owner):
        self.owner = owner

class CupStack:
    def __init__(self):
        # The internal list used to hold our cups
        self._cups = []
        
    def push(self, cup):
        self._cups.append(cup)  # Push to the top of the stack
        
    def pop(self):
        # Safety check: do not pop if the stack is empty!
        if self.is_empty():
            print("Action Blocked: The stack is empty!")
            return None
        return self._cups.pop()  # Pop from the top of the stack
        
    def is_empty(self):
        return len(self._cups) == 0

# Example 2
stack = []
stack.append("Cup A") # Push
stack.append("Cup B") # Push
print(stack.pop())    # Pop (LIFO)

# Step 2: The Horizontal Conveyor Chute (Queue / FIFO)
# A Queue operates on the First In, First Out (FIFO) principle. We implement a queue inside a class using two primary methods:

# enqueue(item): Adds an item to the back of the list using .append().
# dequeue(): Removes the very first item in our list using .pop(0).

# usagge

class CupQueue:
    def __init__(self):
        self._cups = []
        
    def enqueue(self, cup):
        self._cups.append(cup)  # Add to the back of the line
        
    def dequeue(self):
        if self.is_empty():
            print("Action Blocked: The conveyor chute is empty!")
            return None
        return self._cups.pop(0)  # Remove from the front of the line (Index 0)
        
    def is_empty(self):
        return len(self._cups) == 0
queue = ["Cup A", "Cup B"]
print(queue.pop(0)) # Dequeue
print(queue)

    # Example 1

class CupQueue:
    
    def __init__(self):
        self._cups = []
    def dequeue(self):
        return self._cups.pop(0)  # Index 0 is always the oldest item

queue = ["Cup A", "Cup B"]
print(queue.pop(0)) # Dequeue
print(queue)

# ASSIGNMENT
# 1
# 1. Why list.pop(0) is Slow for Large Lists

# Python lists are dynamic contiguous arrays in memory. When you call .pop(0) on a standard list:

# Memory Shift: Python removes the element at index 0 and 
# must shift every remaining element one position to the left to keep the array contiguous.

# 2
# 2. What a Double-Ended Queue (deque) Is 
# In Python's collections module, a deque (pronounced "deck") is a double-ended queue implemented underlyingly as a 
# doubly linked list of fixed-size blocks.$O(1)$ Complexity: 
# It allows appending and popping elements from both ends in O(1) amortized time without shifting remaining items in memory.

from collections import deque

# Initialize a high-performance FIFO queue
queue = deque(["Alice_Latte", "Bob_Espresso", "Charlie_Mocha"])

# Enqueue a new item (adds to the right)
queue.append("David_Cappuccino")

# Dequeue the oldest item in O(1) time (removes from the left)
next_customer = queue.popleft()  # Returns "Alice_Latte"
print(next_customer)