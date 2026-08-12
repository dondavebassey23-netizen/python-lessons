#  Step 1: Defining Instance Methods
# An instance method is a function written inside the indented body of a class. It looks exactly like a standard function, but it has one key difference: the first parameter must always be self.

class CardboardCup:
    def __init__(self, size):
        self.size = size
        self.is_steamed = False
        
    # An instance method that operates on the cup
    def steam_cup(self):
        self.is_steamed = True
        print(f"The {self.size} cup is now steamed and warm.")

my_cup = CardboardCup("medium")
my_cup.steam_cup()

class Cup:
    def greet(self):
        print("Ready for coffee!")

my_cup = Cup()
my_cup.greet()

# Step 2: The Role of self in Methods
# When you call my_cup.steam_cup(), you do not pass any argument into the self parameter. Python automatically passes my_cup into self behind the scenes. This is how the method knows which specific cup's is_steamed attribute to toggle.

class CardboardCup:
    def __init__(self):
        self.is_clean = True
        
    # Always include self as the first parameter
    def rinse_cup(self):
        print("Rinsing the cup...")

my_cup = CardboardCup()
print(my_cup)
my_cup.rinse_cup()



class Cup:
    def check_self(self):
        print(self)

my_cup = Cup()
print(my_cup)
my_cup.check_self()

# Step 3: Modifying Object State
# Methods can take parameters in addition to self to scale and modify internal attribute values.

# Let us track the state of our cardboard cup as we fill it with coffee.

# bject State:
#   - my_cup = [capacity_ounces: 12.0, contents_ounces: 0.0]

class CardboardCup:
    def __init__(self, capacity):
        self.capacity_ounces = capacity
        self.contents_ounces = 0.0
        
    def fill(self, ounces):
        # Modify the attribute in-place using addition assignment
        self.contents_ounces += ounces
        print(f"Filled cup with {ounces} ounces of coffee.")

my_cup = CardboardCup(12.0)
my_cup.fill(8.0)

# Example 2

class Cup:
    def __init__(self):
        self.ounces = 0
    def fill(self, amt):
        self.ounces += amt

my_cup = Cup()
my_cup.fill(5)
my_cup.fill(3)
print(my_cup.ounces)

# Step 4: Adding Safety Gates (Validation)
# If a method modifies state without checking boundaries, it will produce logically invalid states (like having a cup hold $-4$ ounces of liquid, or $15$ ounces in a $12$-ounce cup). We use conditional if checks to block invalid operations.

class CardboardCup:
    def __init__(self, capacity):
        self.capacity_ounces = capacity
        self.contents_ounces = 0.0
        
    def fill(self, ounces):
        # Safety Gate: check if pouring would cause an overflow
        if self.contents_ounces + ounces > self.capacity_ounces:
            print("Action Blocked: Spill Warning! This will overflow.")
        else:
            self.contents_ounces += ounces
            print(f"Successfully filled cup. Current level: {self.contents_ounces} oz")

my_cup = CardboardCup(12.0)
my_cup.fill(8.0)

# EG 3 

class Cup:
    def __init__(self):
        self.ounces = 5
    def drink(self, amt):
        if amt > self.ounces:
            print("Not enough liquid!")
        else:
            self.ounces -= amt

my_cup = Cup()
my_cup.drink(10)
print(my_cup.ounces)