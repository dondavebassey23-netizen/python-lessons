# flavors = ["Vanilla", "Caramel", "Hazelnut"]
# flavors = flavors.append("Mint")
# print(flavors) # this will return none

# Step 1: Mutability (Changing Items in Place)

flavors = ["Vanilla", "Caramel", "Hazelnut"]

# Swap out the bottle in slot 1 (Caramel) for Mocha
flavors[1] = "Mocha"
print(flavors) # Output: ['Vanilla', 'Mocha', 'Hazelnut']

# EG 2
syrups = ["Vanilla", "Mocha"]
syrups[0] = "Mint"
print(syrups)

# Step 2: Adding Elements with .append()
# The .append() method adds a new item to the very end of your list. It modifies your list in-place and returns None.

flavors = ["Vanilla", "Caramel"]

# Add Mint to the far right end of the rack
flavors.append("Mint")
print(flavors) # Output: ['Vanilla', 'Caramel', 'Mint']

# eg 2

stock = ["Cup", "Lid"]
stock.append("Sleeve")
print(len(stock))

# Step 3: Removing Elements with .pop() and .remove()
# .pop(index): Removes the item at a specific index and hands it back to you (returns it). If you do not provide an index, it pops the very last item.
#.remove(item_name): Searches from left to right and deletes the first item that matches item_name. It returns None.

flavors = ["Vanilla", "Caramel", "Hazelnut", "Mocha"]

# 1. Pop by index: Remove slot 1 and save the bottle
popped_bottle = flavors.pop(1) # Removes "Caramel"
print(popped_bottle) # Output: Caramel

# 2. Remove by name: Find "Mocha" and discard it
flavors.remove("Mocha")
print(flavors) # Output: ['Vanilla', 'Hazelnut']

flavors = ["Vanilla", "Caramel"]

if "Mint" in flavors:
    flavors.remove("Mint")
else:
    print("Mint is not on the rack. No action taken.")

# Eg 2
items = ["Vanilla", "Mocha", "Mint"]
last_item = items.pop()
print(last_item)
items.remove("Vanilla")
print(items)

# Step 4: Sorting a List with .sort()
#The .sort() method rearranges the items inside your list in-place. 
# By default, it sorts strings alphabetically and numbers from lowest to highest. Like append, .sort() returns None.

# Rack State:
flavors = ["Vanilla", "Caramel", "Hazelnut"]
# Rearrange the bottles in-place alphabetically
flavors.sort()
print(flavors)

prices = [4.50, 3.50, 5.00]
prices.sort()
print(prices)

# DIFF BW .sort() and sorted()
prices = [45, 12, 85, 32]
result = prices.sort()

print(prices)  # Output: [12, 32, 45, 85] (Original changed!)
print(result)  # Output: None (Do not assign this to a variable!)

# sorted()

prices = [45, 12, 85, 32]
new_prices = sorted(prices)

print(prices)      # Output: [45, 12, 85, 32] (Original untouched!)
print(new_prices)  # Output: [12, 32, 45, 85] (New sorted list created!)
