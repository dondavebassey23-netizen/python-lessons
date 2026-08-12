# Merge Sort: Splitting the row of cups in half recursively until you have single cups, and then merging them back together in perfect sorted order.
# Quicksort: Selecting a single cup as a "Pivot" and partitioning the rest so that all cheaper cups go left, and all more expensive cups go right.

# Step-by-Step Implementation
# Step 1: Merge Sort (Split and Merge)
# Merge Sort is a recursive algorithm.

# The Base Case: If the list has a length of 0 or 1, it is already sorted; return it.
# The Split: Calculate the midpoint, split the list in half, and recursively call merge_sort on both halves.
# The Merge: Call a helper function to merge the two sorted halves back into a single sorted list.

# sorted_list = merge_sort(original_list)

def merge_sort(arr):
    # 1. BASE CASE
    if len(arr) <= 1:
        return arr
        
    # 2. THE SPLIT (Divide)
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])   # Sort the left side recursively
    right_half = merge_sort(arr[mid:])  # Sort the right side recursively
    
    # 3. THE COMBINE (Conquer)
    return merge_sort(left_half, right_half) # Merge the two sorted halves
# A simple slice test to see how we split lists in half
prices = [4.50, 3.50, 5.00, 2.00]
mid = len(prices) // 2
print(prices[:mid])
print(prices[mid:])

# Step 2: The Merge Helper Logic
# The merge(left, right) helper function takes two pre-sorted lists and combines them into a single sorted list by comparing their front elements one by one.

def merge(left, right):
    sorted_list = []
    i = 0  # Pointer for the left list
    j = 0  # Pointer for the right list
    
    # Compare the front elements of both lists and copy the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
            
    # Copy any remaining items from both lists
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

list_a = [3.50, 4.50]
list_b = [2.00, 5.00]
print(merge(list_a, list_b))

# Step 3: Quicksort (Pivot and Partition)
# Quicksort is an extremely fast algorithm. It selects a "pivot" element and "partitions" the list so that elements smaller than the pivot are placed in a left list, and elements larger are placed in a right list.

def quicksort(arr):
    # 1. BASE CASE
    if len(arr) <= 1:
        return arr
        
    # 2. SELECT PIVOT (We choose the middle cup as the pivot)
    pivot = arr[len(arr) // 2]
    
    # 3. PARTITION (Divide)
    left = [x for x in arr if x < pivot]    # All cups cheaper than the pivot
    middle = [x for x in arr if x == pivot] # All cups equal to the pivot
    right = [x for x in arr if x > pivot]   # All cups more expensive than the pivot
    
    # 4. RECURSIVE CONQUER (Combine)
    return quicksort(left) + middle + quicksort(right)

arr = [4.50, 3.50, 4.00, 2.00]
sorted_arr= quicksort(arr)
print(sorted_arr)

# Example 2

prices = [4.50, 3.50, 5.00, 2.00]
sorted_prices = quicksort(prices)
print(sorted_prices)

# ASSIGNMENT
# 1
# Quicksort is typically faster than Merge Sort in practice because it features excellent cache locality and performs its operations in-place. While both algorithms share an identical average-case time complexity of \(O(n \log n)\), their structural interaction with modern computer hardware creates a stark contrast in real-world benchmarks.

# Cache Locality (specifically spatial locality) refers to a hardware optimization where fetching a specific data item from the main memory (RAM) automatically copies its neighboring elements into the ultra-fast CPU cache at the same time.
