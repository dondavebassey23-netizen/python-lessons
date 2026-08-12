# LESSON 18.1: LISTS – CREATION, INDEXING, SLICING

# Step 1: Creating a List
#To create a list in Python, you wrap your items in square brackets [ and ], and separate each item with a comma. You can store strings, integers, floats, or even other variables inside.

# Items are separated by commas and enclosed in square brackets
flavors = ["Vanilla", "Caramel", "Hazelnut"]
print(flavors) # Output: ['Vanilla', 'Caramel', 'Hazelnut']


syrups = ["Vanilla", "Mocha"]
print(type(syrups))

# Step 2: Accessing Elements with Indexing
# You access a single item from a list by typing the list's variable name followed by the item's index number in square brackets.

#Index:      0          1          2          3         4
Bottle:  "Vanilla"  "Caramel"  "Hazelnut"  "Mocha"   "Mint"
#N-Index:   -5         -4         -3         -2        -1

# Example 1
first_bottle = flavors[0] # Slot 0 is the very first position
print(first_bottle)

# Example 2
syrups = ["Vanilla", "Caramel", "Hazelnut"]
print(syrups[0])
print(syrups[-1])

# Step 3: Slicing a List
#Slicing extracts a new, smaller list from your original list. You define a start index and a stop index using a colon inside the brackets: [start:stop].

# The start index is included in the slice.
# The stop index is excluded (Python stops cutting before this index).

flavors = ["Vanilla", "Caramel", "Hazelnut", "Mocha", "Mint"]

# Grab a subset of bottles from slot 1 to slot 3
specialty_set = flavors[1:4] # Starts at 1, stops before index 4
# specialty_set becomes: ["Caramel", "Hazelnut", "Mocha"]
print(specialty_set)

# EG 2
syrups = ["Vanilla", "Caramel", "Hazelnut", "Mocha"]
print(syrups[1:3])

# Step 4: Handling IndexErrors
#If you try to access an index position that does not exist, Python will halt the program and throw an IndexError.

# syrups = ["Vanilla", "Caramel", "Hazelnut", "Mocha"]
# print(syrups[5])

# rEVERSE SLICE

bottles = ["A", "B", "C", "D", "E", "F"]
every_second = bottles[::2] # ------> [START: STOP: STEP]
print(every_second)
# Output: ['A', 'C', 'E']

#Reverse a List InstantlyTo reverse an entire list using a negative step, omit the start and stop indices and use -1:
#python 
reversed_list = bottles[::-1]
print(reversed_list)
# Output: ['F', 'E', 'D', 'C', 'B', 'A']