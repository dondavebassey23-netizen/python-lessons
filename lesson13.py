#Step 1: Functions with Multiple Parameters
# A function can accept multiple parameters separated by commas inside its parentheses. 
# These variables are local to the function and can be used anywhere inside its indented body.
# def make_drink(name, drink):
#     # Use the parameter variables exactly as they are passed
#     print(f"Serving {drink} to {name}")

# make_drink("Alice", "Latte")

## Step 2: Positional Arguments (Arguments in Order)
#By default, Python maps arguments to parameters based on their physical position in the function call. 
# The first argument goes to the first parameter, the second to the second, and so on.
def mix_ingredients(liquid, powder):
    print("Mixing " + liquid + " with " + powder)

mix_ingredients("milk", "cocoa")

def print_receipt(item, cost):
    print(item + ": ₦" + str(cost))

# Run it in order
print_receipt("Espresso", 4.50)

# Step 3: Keyword Arguments (Arguments by Name)
#Keyword arguments allow you to ignore positional sequence entirely by explicitly stating the parameter name and its assigned value inside the function call: parameter_name=value.
def brew_cup(drink, size, temperature):
    print(f"Brewing a {temperature} {size} {drink}...")

# Call using explicit names. The order of these lines does not matter!
brew_cup(temperature="iced", drink="cappuccino", size="medium")

# try this
def cup_label(name, drink):
    print(name + " ordered " + drink)

cup_label(drink="espresso", name="David")

# Step 4: Default Parameter Values
#To make some arguments optional, you can assign default fallback values directly to the parameters inside the function definition using =.
#Required parameters must always be written before default parameters.

# Required parameters come first; default parameters are placed at the end
def process_order(name, drink, size="medium", milk="whole"):
    print(f"Order for {name}: {size} {drink} with {milk} milk.")

process_order("David", "caprison")

# Required fields are declared first, optional default fields are placed last
def process_order(name, drink, size="medium"):
    print(f"{name} wants a {size} {drink}")

# Now we can safely omit the optional size argument
process_order("Alice", "Latte") # Uses the default "medium"
process_order("Bob", "Espresso", "large") # Overrides the default

def sprinkle_sugar(packets=1):
    print("Adding " + str(packets) + " sugar packets.")

sprinkle_sugar()
sprinkle_sugar(3)

#Step 5: Mixing Positional and Keyword Arguments
#You can mix both positional and keyword arguments in a single function call, but positional arguments must always be passed first. 
#Once you use a keyword argument, all remaining arguments after it must also be passed as keyword arguments.

def label(name, drink, size="medium"):
    print(name + " wants a " + size + " " + drink)

# Attempt to place a positional argument AFTER a keyword argument
label(name="David", drink="espresso" )

# *args 
def sum_numbers(*args):
    # args is a tuple containing (10, 20, 30)
    print(f"Received tuple: {args}")
    return sum(args)

result = sum_numbers(10, 20, 30)
print(f"Total: {result}")

# **kwargs

def build_user_profile(**kwargs):
    # kwargs is a dict containing {"name": "Alice", "role": "Admin", "level": 5}
    print(f"Received dictionary: {kwargs}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

build_user_profile(name="Alice", role="Admin", level=5)

def add_toppings(*args):
    print("Toppings added:", args)

add_toppings("chocolate", "sprinkles", "whipped cream")