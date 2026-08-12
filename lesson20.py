# LESSON 20.1: TUPLES
# Step 1: Creating a Tuple
#To create a tuple in Python, you wrap your items in parentheses ( and ) instead of square brackets, separating each item with a comma.

single_item = ("Vanilla",)
print(type(single_item))

# Step 2: Tuple Indexing
# You access elements inside a tuple using the exact same 0-based indexing bracket notation as lists.

signature = ("Vanilla", "Caramel", "Hazelnut")
print(signature[1])
print(signature[-1])

# Step 3: Immutability and Safety
# Because tuples are immutable, they do not support any modification methods. Tuples do not have .append(), .pop(), .remove(), or .sort() methods. 
# Any attempt to write to or modify a tuple will cause a crash.

# signature_blend = ("Vanilla", "Caramel", "Hazelnut")

# # Attempt to swap out an item
# signature_blend[1] = "Mocha" # this will crash as Tuple dose not support item assignment

signature_blend = ("Vanilla", "Caramel", "Hazelnut")

# We read the recipes without modifying the parent tuple
print(f"To make the House Blend, use: {signature_blend[0]} and {signature_blend[1]}")

# signature = ("Vanilla", "Caramel")
# # Try to append:
# signature.append("Hazelnut")
#Observe how Python immediately throws an AttributeError, confirming that tuples lack modification methods.

 
#  Step 4: Tuple Unpacking
# Tuple unpacking allows you to assign all elements of a tuple to individual, distinct variables in a single line of code. 
# The number of variables on the left of the = must match the number of elements in the tuple exactly.

#EXAMPLE 1
#System State:
signature_recipe = ("Vanilla", "Caramel", "Hazelnut")
left_pump = ""
center_pump = ""
right_pump = ""

left_pump,center_pump,right_pump = signature_recipe
print(left_pump)
print(center_pump)
print(right_pump)

# EXAMPLE 2

dimensions = (12, 8)
width, height = dimensions
print(width)
print(height)