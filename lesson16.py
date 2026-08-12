# LESSON 16.1: ANONYMOUS FUNCTIONS (LAMBDA)
look = lambda p:p ** 4
print(look(4))

#Step 2: The Implicit Return (No return Keyword)
# Omit the word "return" completely. The division is returned automatically.
scale_syrup = lambda ml: ml / 30.0

print(scale_syrup(60.0)) # Output: 2.0

new_price = lambda x : x / 4.0
print(new_price(70.0))

# Correct
greet = lambda name: "Hello, " + name
print(greet("David"))

#Step 3: The Single Expression Limit
# A lambda function can only hold one single expression. 
# It cannot contain multiple statements, loops, or complex multi-line logic blocks.

#Dispenser State:
sugar_level = "High"
# We can use a single-line "ternary" conditional inside a lambda
get_pump_count = lambda level: 4 if level == "High" else 2

pumps_to_dispense = get_pump_count(sugar_level)
print(pumps_to_dispense)

#Dispenser State (New):
pumps_to_dispense = 4

check_size = lambda ounces: "large" if ounces >= 16 else "small"
print(check_size(12))
print(check_size(16))