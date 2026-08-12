
# def steam_milk():
#     temp = 65  # local variable
#     print(f"Milk steamed to {temp} degrees.")

# steam_milk()
# print(f"The final temperature was {temp}") # this code did not run because at the first print , the tempreture was destroyed when it first ran.


def steam_milk():
    temp = 65  # local variable

# Step 1: Local Scope (Variables Inside Functions)
#Any variable created inside a function belongs to that function's local scope. 

def steam_milk():
    temp = 65

    print(f"Milk steamed to {temp} degrees.")
    return temp  # Hand the value back before the napkin is destroyed!

# Capture the returned value in a global variable

final_temp=steam_milk()
print(f"The final temperature was {final_temp}")

def test_scope():
    secret_recipe = "Vanilla Syrup"
    print(secret_recipe)
    return secret_recipe

new_scope=test_scope()
# Now try to print it outside:
print(new_scope)

# Step 2: Global Scope (Variables Outside Functions)

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

shop_name = "Espresso Cart"
def print_shop():
    print("Welcome to " + shop_name)

print_shop()

# Step 3: The global Keyword (Modifying Global Variables)
# To modify a global variable from inside a function, you must declare it with the global keyword at the very beginning of the function body. 
# This tells Python: "Do not create a new local napkin note. Use the whiteboard variable on the wall."
# EXAMPLE 1
shop_name = "Espresso Cart"
def print_shop(new_shop_name):
    global shop_name
    shop_name = new_shop_name
    print("Welcome to " + shop_name)

print_shop("Candy cart")

# EXAMPLE 2
menu_price = 4.50  # Global

def update_price(new_price):
    global menu_price  # Link this function to the global whiteboard variable
    menu_price = new_price  # This now updates the global whiteboard!
    print(f"Whiteboard price updated to ₦{menu_price:.2f}")

update_price(5.00)
print(f"Current menu price is now: ₦{menu_price:.2f}") # Output: 5.00

# EXAMPLE 3
total_sales = 0.0  # Global
total_sales = 23.56  # Global


def record_sale(amount):
    global total_sales  # Explicitly link to the global variable
    total_sales = total_sales + amount
    print(f"Sale recorded: ₦{amount:.2f}")

record_sale(4.50)
print(f"Register total sales: ₦{total_sales:.2f}")


# EXAMPLE 4


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

# Step 5: The nonlocal Keyword (Modifying Enclosing Scopes)
#When you write a nested function (a function inside a function), the inner function can read variables inside the outer parent function. #To modify those parent variables, the inner function must declare them using the nonlocal keyword.

# EXAMPLE 1
def run_coffee_cart():
    # Outer parent function's local variable
    current_order = "Espresso"
    
    def change_order(new_drink):
        nonlocal current_order  # Link to the parent function's variable
        current_order = new_drink
        print(f"Order updated to: {current_order}")
        
    change_order("Latte")
    print(f"Final cart order: {current_order}")

run_coffee_cart()

# TRY 
def outer():
    x = "original"
    def inner():
        nonlocal x
        x = "modified"
    inner()
    print(x)

outer()

# Step 6: Scope Summary (The LEGB Rule)
# Python looks up variables in a strict order of scopes, known as the LEGB hierarchy:

# Local: Inside the current function.
# Enclosing: Inside any parent nested functions.
# Global: Outside all functions at the top level of the file.
# Built-in: Python's pre-installed names (like print or len).
