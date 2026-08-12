# Step 1: The Anatomy of a Recursive Function
def wash_mugs(stack_size):
    # 1. BASE CASE (The Stop Switch)
    if stack_size == 0:
        print("All mugs are washed! Drying hands.")
        return  # Stop the function completely
        
    # 2. RECURSIVE CASE (Action + Shrink)
    print(f"Washing mug number {stack_size}...")
    
    # Call ourselves with one less mug!
    wash_mugs(stack_size - 1)
wash_mugs(3)



def wash_mugs(stack_size):
    if stack_size <= 0:  # Base case catches zero and negative safety boundaries
        print("Stack is empty!")
        return
        
    print(f"Washing mug {stack_size}")
    wash_mugs(stack_size - 1)  # Safely approaches the base case

wash_mugs(3)



def count_down(cups):
    if cups <= 0:
        print("Done!")
        return
    print("Cup: " + str(cups))
    count_down(cups - 1)

count_down(3)

# Step 2: The Base Case (The Stop Switch)
# The base case must always be written first inside the function body. 
# If you place the recursive call before the base case, the computer will call itself recursively before ever checking if it should stop.

def washing(jugs):
    if jugs <= 0:
        print('Done washing')
        return
    print("jugs: " + str(jugs))
    washing(jugs - 1)
    
washing(3)

def clean_stack(mugs):
    if mugs <= 0:  # Check the stop switch first!
        return
        
    print("Cleaning...")
    clean_stack(mugs - 1)
clean_stack(4)


# Step 3: Tracing the Call Stack (The State Transition)
# System State:
stack_size = 3
total_water_ml = 0

def calculate_water(mugs):
    if mugs <= 0:
        return 0  # Base case: 0 mugs require 0 ml
        
    # Recursive Case: 10ml for the current mug + water for the rest of the stack
    return 10 + calculate_water(mugs - 1)

total_water_ml = calculate_water(stack_size)

print(calculate_water(3))

# System State (New):
stack_size = 3
total_water_ml = 30

def sum_stack(mugs):
    if mugs <= 0:
        return 0
    return mugs + sum_stack(mugs - 1)

print(sum_stack(4))