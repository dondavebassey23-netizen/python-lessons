# Step 1: Defining a Class
# To define a class in Python, you use the class keyword followed by the name of your class. By convention, class names are written in PascalCase (capitalizing the first letter of every word, like CoffeeCup).

# Define the master blueprint class
class CoffeeCup:
    # A simple placeholder pass statement for now
    pass
print(CoffeeCup)

class KioskMachine:
    pass

print(KioskMachine)

# Step 2: Creating Instances
# To stamp out an actual, physical object from your class blueprint, you call the class name followed by parentheses (). This process is called Instantiation.

class CoffeeCup:
    pass

# Stamp out two separate cup instances from the blueprint
cup_1 = CoffeeCup()
cup_2 = CoffeeCup()

print(type(cup_1)) # Output: <class '__main__.CoffeeCup'>

# eg 2
class Cup:
    pass

my_cup = Cup()
print(my_cup)

# Step 3: Initializing Attributes with __init__ and self
# When you stamp out a new cup, you want to immediately define its properties (like size and owner). We do this inside the class using a special method named __init__ (short for initialize).
# The first parameter of __init__ must always be self, which represents the specific cup currently being manufactured.

class CoffeeCup:
    # The constructor runs automatically when a cup is stamped out
    def __init__(self, size, owner):
        # self.attribute = parameter
        self.size = size          # Write the size on this specific cup
        self.owner = owner        # Write the owner on this specific cup
        self.contents = "empty"   # Default starting state for all cups

    def __str__(self):
        return f"{self.owner}'s {self.size} cup ({self.contents})"  # this line is to print something meaningful
     

bobs_cup = CoffeeCup("small","Bob", )
print(bobs_cup)

# E.g 2
class CoffeeCup:
    def __init__(self, size, owner):
        self.size = size  # "self" binds the data to the specific object
        self.owner = owner

# Create a cup, passing values for size and owner
alice_cup = CoffeeCup("large", "Alice")
print(alice_cup.size) # .size or . owner will print the size of the cupo , or the owner

# E.g 3
class Cup:
    def __init__(self, colour):
        self.colour = colour

brand_colour = Cup("green")
print(brand_colour.colour)

# Step 4: Accessing and Modifying Attributes
# To read or write data to an object, you use Dot Notation. You write the name of your specific object instance, followed by a dot ., and then the name of the attribute: object_name.attribute_name.

# Object State:
# alice_cup = [size: "small", owner: "Alice", contents: "empty"]

class CoffeeCup:
    def __init__(self, size, owner, contents):
        self.size = size
        self.owner = owner
        self.contents = contents
        
    # def __repr__(self):
    #     return f'[size: "{self.size}", owner: "{self.owner}", contents: "{self.contents}"]' THIS IS A DUNDER __repr__

# 1. Accessing: Read the owner of the cup
customer = alice_cup.owner

# 2. Modifying: Overwrite the cup contents in-place
alice_cup.contents = "Espresso"

alice_cup = CoffeeCup("small", "Alice", "Espresso")

print(customer)
print(alice_cup.contents)

# EG 4 attribute modification
class Cup:
    def __init__(self):
        self.contents = "empty"

my_cup = Cup()
my_cup.contents = "Mocha"
print(my_cup.contents)

class Cup:
    def __init__(self, size, owner):
        self.size = size
        self.owner = owner
    def __str__(self):
        return f"{self.owner}'s cup is {self.size}"

angela_cup = Cup("Small", "Angela")
print(angela_cup)