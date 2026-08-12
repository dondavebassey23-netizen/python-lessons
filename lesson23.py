# Step 3: Dictionary Comprehensions
# To generate a new dictionary in-place, you use curly braces { and } and define both a key expression and a value expression separated by a colon: {key_expr: value_expr for key, value in source_dict.items()}.

# Example 1

menu = {"Latte": 4.50, "Espresso": 3.50, "Mocha": 5.00}

# Apply a ₦0.50 discount to every value on the menu whiteboard
discounted_menu = {drink: price - 0.50 for drink, price in menu.items()}

print(discounted_menu) # Output: {'Latte': 4.0, 'Espresso': 3.0, 'Mocha': 4.5}

# Example 2 
stock = {"cups": 100, "lids": 150}
double_stock = {item: count * 2 for item, count in stock.items()}
print(double_stock)

# Step 4: Set Comprehensions
# A set comprehension works exactly like a list comprehension, but it is wrapped in curly braces { and } (without colons). This tells Python to automatically de-duplicate any identical values produced during the loop.

 # Example 1

#  System State:
raw_spices = {"  cinnamon ", "cocoa ", "cinnamon", "nutmeg"}
clean_spices = {}

# Strip spaces and normalize to lowercase in-place
clean_spices = {spice.strip().lower() for spice in raw_spices}
print(clean_spices)

# Example 2

messy_names = ["LATTE", "latte", "espresso", "latte"]
unique_clean = {name.lower() for name in messy_names}
print(unique_clean)

# The ternary operator (value_if_true if condition else value_if_false) can be used inside a list comprehension to transform every item in a list based on a condition.When you combine them, the if-else block must be placed before the for loop syntax.

# the syntax structure 
#[true_value if condition else false_value for item in iterable]

# Assignment
 # no 1a

# The Rule: A conditional expression must always return a value, which requires both an if and an else.

# When you place an if statement at the very end of a comprehension, it acts strictly as a filter clauses syntax.The Rule: It decides whether an item is allowed into the list at all. It cannot have an else branch because you cannot say "if the item doesn't qualify, include this other random thing instead" at the filtering stage.How Python reads it: "Loop through the items. If an item passes this trailing condition, keep it. Otherwise, drop it completely." 


# Explain how to write an if/else conditional inside a list comprehension (e.g. [x if x > 2 else 0 for x in list]).
numbers = [1, 2, 5, 6]

new_numbers = [ x if x > 2 else 0 for x in numbers ]
print(new_numbers)

# assignm,ent 2
# Write a comprehension that converts a list of sizes: any "large" becomes "Premium", and any other size becomes "Regular".

list_of_sizes = ["small", "Premium" "medium", "large", "extra_large"]
new_sizes = ["Premium" if size == "large" else "Regular" for size in list_of_sizes]

print(new_sizes)
# LESSON 23.1: COMPREHENSIONS (LIST, DICT, SET)

#Comprehension: A concise Python syntax that creates a new collection 
# by evaluating an inline loop over an existing collection.

# Step 1: List Comprehensions (Transforming Lists)
# A list comprehension is written inside standard square brackets [ and ]. 
# It contains three essential parts:

# The Expression: What you want to do to each item (e.g., pumps * 2).
# The Loop Variable: The temporary placeholder name (e.g., p).
# The Iterable: The source list you are reading from (e.g., pumps).

# The Syntax: [expression for variable in source_list]
standard_pumps = [1, 2, 3]
doubled_pumps = [p * 2 for p in standard_pumps]

print(doubled_pumps) # Output: [2, 4, 6]

# Example 2
prices = [3.00, 4.00, 5.00]
taxed_prices = [p * 1.10 for p in prices]
print(taxed_prices)

# Step 2: Filtering Inside List Comprehensions
# To filter out items from your source list, you add an if statement to the very end of your comprehension. 
# Python will evaluate the condition for each item, only keeping the ones that return True.

# The Syntax: [expression for variable in source_list if condition]
ordered_sizes = ["small", "large", "medium", "large", "small"]

# We only want to prepare "large" cups
large_only = [size for size in ordered_sizes if size == "large"]

print(large_only) # Output: ['large', 'large']
