# Step 1: Local Scope (Variables Inside Functions)
#Any variable created inside a function belongs to that function's local scope. 

def steam_milk():
    temp = 65
    print(f"Milk steamed to {temp} degrees.")
    return temp  # Hand the value back before the napkin is destroyed!

# Capture the returned value in a global variable
# final_temp = steam_milk()
# print(f"The final temperature was {final_temp}")

# def test_scope():
#     secret_recipe = "Vanilla Syrup"
#     print(secret_recipe)

# test_scope()
# Now try to print it outside:
#print(secret_recipe) # this code crashed, becased secret_recipe was not defined 


# Step 2: Global Scope (Variables Outside Functions)
#Variables declared outside of any function belong to the global scope. 
#They live from the moment they are created until the entire script finishes running, and they can be read from anywhere inside your file.

# Global variable (written on the public whiteboard)
menu_price = 4.50

def serve_customer(name):
    # We can read the global variable naturally
    print(f"Charging {name} ₦{menu_price:.2f} for their latte.")

serve_customer("Alice")

total_sales = 23.56  # Global

def record_sale(amount):
    global total_sales  # Explicitly link to the global variable
    total_sales = total_sales + amount
    print(f"Sale recorded: ₦{amount:.2f}")

record_sale(4.50)
print(f"Register total sales: ₦{total_sales:.2f}")



count = 0
def increment():
    global count
    count = count + 1
    print(count)

increment()
increment()


# Step 4: Variable Lifetime (Birth and Death of Variables)

global_sales = 0
def make_drink():
    local_count = 0  # Born fresh on every function call
    global global_sales
    
    local_count = local_count + 1
    global_sales = global_sales + 1
    print(f"Local: {local_count}, Global: {global_sales}")

make_drink()
make_drink()





