# # SET

# Step 1: Set Creation and Uniqueness
# To create a set in Python, you wrap your unique elements in curly braces { and }. 
# Unlike dictionaries, you do not use colons because there are no mapped keys.

# Create a set of displaying ingredients
specials_tray = {"Cinnamon", "Cocoa", "Vanilla"}

# The Duplicate Filtering Rule
# If you attempt to define a set with duplicate items, 
# Python silently ignores the duplicates and stores only one instance of each in memory:

# We try to add duplicate "Cinnamon" items
specials_tray = {"Cinnamon", "Cocoa", "Cinnamon", "Vanilla", "Cocoa"}

print(specials_tray) # Output: {'Cinnamon', 'Cocoa', 'Vanilla'}

# Special Case: The Empty Set
# To create an empty set, you must use the set() constructor. 
# Using empty curly braces {} creates an empty dictionary.

# This creates a Dictionary!
bad_empty = {}

# This creates a Set!
good_empty = set()

items = {"Cocoa", "Cocoa", "Vanilla"}
print(items)
print(len(items))

# Step 2: Membership Testing (in and not in)
# USING IN AND NOT IN
specials_tray = {"Cinnamon", "Cocoa", "Vanilla"}

# Fast check if Cinnamon is on display
has_cinnamon = "Cinnamon" in specials_tray  # -> True
has_nutmeg = "Nutmeg" in specials_tray      # -> False

# (Using Membership Checks)
specials_tray = {"Cinnamon", "Cocoa", "Vanilla"}

# Safely check membership
if "Cinnamon" in specials_tray:
    print("Sprinkling cinnamon on the drink...")

# Example 3
toppings = {"Cinnamon", "Cocoa"}
print("Cinnamon" in toppings)
print("Nutmeg" not in toppings)

# Step 3: Set Operations: Union (|) and Intersection (&)
# Set operations allow you to compare and combine whole trays of ingredients instantly:

# Union (|): Combines all unique items from both trays.
# Intersection (&): Keeps only the items that are present on both trays.

my_tray = {"Cinnamon", "Cocoa"}
assistant_tray = {"Cocoa", "Nutmeg", "Vanilla"}

# 1. Union: Find all unique toppings available at our cart
all_toppings = my_tray | assistant_tray
print(all_toppings) # Output: {'Cinnamon', 'Cocoa', 'Nutmeg', 'Vanilla'}

# 2. Intersection: Find which toppings both trays have in common
matching_toppings = my_tray & assistant_tray
print(matching_toppings) # Output: {'Cocoa'}

# Example
set_a = {"Vanilla", "Mocha"}
set_b = {"Mocha", "Mint"}
print(set_a | set_b)
print(set_a & set_b)

# Step 4: Set Operations: Difference (-)
# The difference operator (-) subtracts the items of the second set from the first set, 
# returning a new set containing only the items that are unique to the first tray.

# System State:
my_tray = {"Cinnamon", "Cocoa", "Vanilla"}
assistant_tray = {"Cocoa", "Nutmeg"}
unique_to_me = {}

# Subtract the assistant's items from my tray
unique_to_me = my_tray - assistant_tray
print(unique_to_me)

# Example 4
set_a = {"Vanilla", "Caramel", "Mocha"}
set_b = {"Caramel"}
print(set_a - set_b)


# using .add() and update()

# 2. Adding a Single Bottle using .add()
#To add a single item "Mint" into your specials set:
specials_tray = {"Cinnamon", "Cocoa", "Vanilla"}

specials_tray.add("Mint")

print(specials_tray)
# Output: {'Cinnamon', 'Cocoa', 'Vanilla', 'Mint'}

# 3. Merging Multiple Items using .update()
#To merge a list containing ["Cocoa", "Vanilla-Sugar"] into your existing set:
specials_tray = {"Cinnamon", "Cocoa", "Vanilla"}
backup_items = ["Cocoa", "Vanilla-Sugar"]

specials_tray.update(backup_items)

print(specials_tray)
# Output: {'Cinnamon', 'Cocoa', 'Vanilla', 'Vanilla-Sugar'}

# Note: Passing a string to .add("Mint") inserts "Mint". However, 
# if you pass a string to .update("Mint"), 
# Python treats the string as an iterable 
# and adds each individual character ('M', 'i', 'n', 't') into the set.