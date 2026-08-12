# LESSON 21.1: DICTIONARIES

# Step 1: Creating a Dictionary
# To create a dictionary in Python, you wrap your key-value pairs in curly braces { and }. 
# Each key is separated from its value by a colon :, and each pair is separated from the next by a comma. Keys are typically strings, 
# while values can be any data type (integers, floats, strings, or lists).


# EXAMPLE 1
# Create a menu dictionary (mapping drink keys to float prices)
menu = {
    "Latte": 4.50,
    "Espresso": 3.50,
    "Mocha": 5.00
}

print(menu)


# EXAMPLE 2
# Colons link keys to values; commas separate the pairs
menu = {
    "Latte": 4.50,
    "Espresso": 3.50
}
print(menu) # Output: {'Latte': 4.5, 'Espresso': 3.5}

# TO know the data type
inventory = {"cups": 100, "lids": 150}
print(type(inventory))

# Step 2: Accessing Values by Key
# To retrieve a value from a dictionary, you write the dictionary name followed by the specific key in square brackets [].

menu = {
    "Latte": 4.50,
    "Espresso": 3.50
}

# Look up the price of a Latte
latte_price = menu["Latte"]
print(latte_price) # Output: 4.5

# Example 2
lands = {
    "imoh" : 80,
    "abasido" : 784,
    "afokang" : 872
}

land_price = lands["abasido"]
print(land_price)


# (Accessing by Named Key)
# Access the value using its explicit string key
first_price = menu["Latte"]
print(first_price) # Output: 4.5

#Example 2 

stock = {"cups": 100, "lids": 150}
print(stock["cups"])

# Step 3: Updating and Adding Values
# Dictionaries are mutable. You can update an existing value or add 
# a brand-new key-value pair using the exact same bracket syntax: dictionary_name[key] = value.

# If the key already exists, Python overwrites the old value.
# If the key does not exist, Python automatically adds the new key-value pair to the dictionary.

# Example 1
stock = {"cups": 100, "lids": 150}
stock["plates"] = 150 # this line ads plate to the list with he corresponding price
print(stock)


# Example 2

menu = {
    "Latte": 4.50,
    "Espresso": 3.50
}

# 1. Update an existing price (Latte increases to 5.00)
menu["Latte"] = 5.00

# 2. Add a brand-new drink to the board (Chai is added)
menu["Chai"] = 4.00

print(menu) # Output: {'Latte': 5.0, 'Espresso': 3.5, 'Chai': 4.0}

# Example 3

kiosk = {"status": "OFF"}
kiosk["status"] = "ON"      # Update existing
kiosk["operator"] = "Robot" # Add new
print(kiosk)


# Step 4: Handling KeyErrors Safely
# If your script tries to access a key that is missing, the program will crash. 
# To prevent this, you can use two safe search techniques:
# The in Operator: Checks if a key exists on the board before attempting to access it.
# The .get() Method: Safely returns None (or a default value of your choice) instead of crashing if the key is missing.

#Menu State:
menu = {"Latte": 4.50, "Espresso": 3.50}
target_drink = "Chai"
resolved_price = 0.0

resolved_price = menu.get(target_drink, 0.0)
print(resolved_price)

# Example 3
menu = {"Latte": 4.50}
print(menu.get("Chai"))       # Prints None
print(menu.get("Chai", 3.00)) # Prints 3.0