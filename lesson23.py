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
