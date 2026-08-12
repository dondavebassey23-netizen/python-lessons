# LESSON 32.1: BASIC SORTING (BUBBLE, INSERTION, SELECTION)

# Step 1: Swapping Elements Safely
# To swap two elements in a list, you must exchange their values simultaneously so neither is overwritten. 
# In Python, you can write this cleanly on a single line:

flavors = ["Mocha", "Latte"]

# The Tuple Swap: Python evaluates both on the right first, then assigns them to the left
flavors[0], flavors[1] = flavors[1], flavors[0]

print(flavors) # Output: ['Latte', 'Mocha'] (Safely swapped!)

# ASSIGNMENT

prices = [4.50, 3.50]
prices[0], prices[1] = prices[1], prices[0]
print(prices)


# Step 2: Bubble Sort (Adjacent Swaps)
# Bubble Sort uses nested loops.

# The outer loop tracks how many passes we make.
# The inner loop compares adjacent items (i and i+1) and swaps them 
# if the left item is greater than the right.

def bubble_sort(arr):
    n = len(arr)
    for pass_num in range(n):
        # The last pass_num items are already sorted at the end
        for i in range(0, n - pass_num - 1):
            if arr[i] > arr[i + 1]:
                # Swap the adjacent cups!
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


# # We stop the loop at n - 1 so that i + 1 always points to a valid index on the tray
# for i in range(0, n - 1):
#     if arr[i] > arr[i + 1]:
#         arr[i], arr[i + 1] = arr[i + 1], arr[i]
# # Why this works: The loop terminates safely before reaching past the far-right edge of the counter.


prices = [4.50, 3.50, 5.00, 2.00]
bubble_sort(prices)
print(prices)

# Step 3: Selection Sort (Scan and Swap)
# Selection Sort scans the unsorted portion of the list, identifies the index of the absolute minimum value, 
# and swaps it with the first item in the unsorted section.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume the current item is the smallest
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update the index of the smallest item found
                
        # Swap the smallest item with the first unsorted item
        arr[i], arr[min_index] = arr[min_index], arr[i]

prices = [4.50, 3.50, 5.00, 2.00]
selection_sort(prices)
print(prices)

# Step 4: Insertion Sort (Slide Into Place)
# Insertion Sort loops through the list from left to right. 
# For each item, it picks it up and slides it backward (left) through the sorted section until it finds its correct relative position.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Pick up the current cup
        j = i - 1
        
        # Slide the cup left as long as the neighboring cup is more expensive
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift the more expensive cup to the right
            j -= 1
            
        arr[j + 1] = key  # Drop the cup into its correct spot

prices = [4.50, 3.50, 5.00, 2.00]
insertion_sort(prices)
print(prices)