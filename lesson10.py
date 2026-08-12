# loops 
# for count in range(3):
#     print("Grind " + str(count))

# weight = 0.0
# while weight < 1.5:
#     weight = weight + 0.2
#     print("Current weight: " + str(weight))

# # Check soil condition dynamically
# while soil_moisture_percentage < 45.0:
#     water_valve_active = True
#     dispense_water(seconds=10)
#     soil_moisture_percentage = read_moisture_sensor() # Update state variable
    
# water_valve_active = False # Safe shutdown

# using break : completely stops and exits the loop
# Use break when you have fulfilled your condition 
# (e.g., finding a target item) and there is no need to keep looping over the remaining items.

# numbers = [1, 3, 5, 8, 9, 11, 18, 41]

# for num in numbers:
#     if num % 2 == 0:
#         print(f"First even number found: {num}")
#         break  # Stops the loop immediately!
#     print(f"Checking: {num}")

# print("Loop finished.")

# using continue : continue skips the rest of the current iteration and jumps to the next cycle.

# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     if num == 3:
#         continue  # Skip printing 3 and jump straight to 4
#     print(f"Processing number: {num}")

# for num in range(2, 45):
#     if num % 2 != 0:
#         continue

#     if num > 9:
#         print(f"Target reached at: {num}")
#         break
#     print(f"processing odd number: {num}")

#using chain() functtion from itertools modules

# # for list of numbers.
from itertools import chain

# first = [2, 5, 7]
# second = [3, 1]
# third = [4, 5, 7]

# for value in chain(first, second, third):
#     print(value**2)

# for list of lists



matrix = [
     [9, 3, 8],
     [4, 5, 2],
     [6, 4, 3],
 ]

for value in chain(*matrix):# (*matrix) * is called unpacking operator
     print(value**2)